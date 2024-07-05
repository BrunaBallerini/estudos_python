# ABSTRAÇÃO -> CONTRATO
from pathlib import Path
import json

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg): # MÉTODO ABSTRATO
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        return self._log(f'ERROR: {msg}')
    
    def log_success(self, msg):
        return self._log(f'SUCCESS: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        msg_formated = f'{msg} - {self.__class__.__name__}'
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formated)
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} - {self.__class__.__name__}')


if __name__ == '__main__':
    l = LogFileMixin()
    l.log_error('message error')
    l.log_success('message success')
    lp = LogPrintMixin()
    lp.log_error('message error')
    lp.log_success('message success')