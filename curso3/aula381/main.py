# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring, no-name-in-module
# pylint: disable=missing-module-docstring, invalid-name
# type: ignore


import sys
import time

from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from ui_worker import Ui_MainWindow


class Worker1(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def run(self):
        value = '0'
        self.started.emit(value)
        for i in range(10):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(1)
        self.finished.emit(value)


class Worker2(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def executeMe(self):
        value = '0'
        self.started.emit(value)
        for i in range(0, 60, 2):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(0.2)
        self.finished.emit(value)


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self.button1.clicked.connect(self.hardWork1)
        self.button2.clicked.connect(self.hardWork2)

    def hardWork1(self):
        # Isso garante que o window vai ter uma referência para worker e thread
        self._worker1 = Worker1()
        self._thread1 = QThread()

        worker1 = self._worker1
        thread1 = self._thread1

        # Step-by-step

        # Worker é movido para a thread. Todas as funções e métodos do
        # objeto de worker serão executados na thread criado pela QThread.
        worker1.moveToThread(thread1)

        # Quando uma QThread é iniciada, emite o sinal started automaticamente.
        thread1.started.connect(worker1.run)

        # O sinal finished é emitido pelo objeto worker quando o trabalho que
        # ele está executando é concluído. Isso aciona o método quit da Qthread
        # que interrompe o loop de eventos dela.
        worker1.finished.connect(thread1.quit)

        # deleteLater solicita a exclusão do objeto worker do sistema de
        # gerenciamento de memória do Python. Quando o worker finaliza, ele
        # emite um sinal finished que vai executar o método deleteLater.
        # Isso garante que objetos sejam removidos da memória corretamente.
        thread1.finished.connect(thread1.deleteLater)
        worker1.finished.connect(worker1.deleteLater)

        # Aqui estão seus métodos e início, meio e fim
        # execute o que quiser
        worker1.started.connect(self.worker1Started)
        worker1.progressed.connect(self.worker1InProgress)
        worker1.finished.connect(self.worker1Finished)

        # Inicie a thread
        thread1.start()

    def worker1Started(self, value):
        self.button1.setDisabled(True)
        self.label1.setText(value)
        print('worker 1 started', value)

    def worker1InProgress(self, value):
        self.label1.setText(value)
        print('work in progress', value)

    def worker1Finished(self, value):
        self.button1.setDisabled(False)
        self.label1.setText(value)
        print('work finished', value)

    def hardWork2(self):
        self._worker2 = Worker2()
        self._thread2 = QThread()

        worker2 = self._worker2
        thread2 = self._thread2

        # Step-by-step

        # Move worker to thread
        worker2.moveToThread(thread2)

        # Run
        thread2.started.connect(worker2.executeMe)

        # Finishing the thread when worker is finished
        worker2.finished.connect(thread2.quit)

        # Remove trash from memory
        thread2.finished.connect(thread2.deleteLater)
        worker2.finished.connect(worker2.deleteLater)

        # Execution
        worker2.started.connect(self.worker2Started)
        worker2.progressed.connect(self.worker2InProgress)
        worker2.finished.connect(self.worker2Finished)

        thread2.start()

    def worker2Started(self, value):
        self.button2.setDisabled(True)
        self.label2.setText(value)
        print('work started')

    def worker2InProgress(self, value):
        self.label2.setText(value)
        print('work in progress')

    def worker2Finished(self, value):
        self.button2.setDisabled(False)
        self.label2.setText(value)
        print('work finished')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MyWindow()
    mainWindow.show()
    app.exec()
