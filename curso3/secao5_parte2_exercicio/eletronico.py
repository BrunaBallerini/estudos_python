from log import LogFileMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome # HERANÇA
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True
        
    def desligar(self):
        if self._ligado:
            self._ligado = False

# COMPOSIÇÃO
# class Smartphone():
#     def __init__(self, nome):
#         self._nome = nome
#         self.eletronico = Eletronico()
#         self.log_print_mixin = LogFileMixin()


#     def ligar(self):
#         self.eletronico.ligar()
#         if self.eletronico._ligado:
#             msg = f'{self._nome} esta ligado'
#             self.log_print_mixin.log_success(msg)

        
#     def desligar(self):
#         self.eletronico.desligar()
#         if not self.eletronico._ligado:
#             msg = f'{self._nome} esta Desligado'
#             self.log_print_mixin.log_error(msg)

# COMPOSIÇÃO E HERANÇA
# class Smartphone(Eletronico):
#     def __init__(self, nome):
#         super().__init__(nome)
#         self.log_file_mixin = LogFileMixin()


#     def ligar(self):
#         super().ligar()
#         if self._ligado:
#             msg = f'{self._nome} esta ligado'
#             self.log_file_mixin.log_success(msg)

        
#     def desligar(self):
#         super().desligar()
#         if not self._ligado:
#             msg = f'{self._nome} esta Desligado'
#             self.log_file_mixin.log_error(msg)

# HERANÇA
class Smartphone(Eletronico, LogFileMixin):
    def ligar(self):
        super().ligar()
        if self._ligado:
            msg = f'{self._nome} esta ligado'
            self.log_success(msg)

        
    def desligar(self):
        super().desligar()
        if not self._ligado:
            msg = f'{self._nome} esta Desligado'
            self.log_error(msg)
