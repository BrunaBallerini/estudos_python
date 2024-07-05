from eletronico import Smartphone

galaxy = Smartphone('Galaxy')

# COMPOSIÇÃO
# galaxy.ligar()
# galaxy.log_print_mixin.log_success('Ligou')
# galaxy.desligar()
# galaxy.log_print_mixin.log_error('Desligou')

# COMPOSIÇÃO E HERANÇA
# galaxy.ligar()
# galaxy.log_file_mixin.log_success('Ligou')
# galaxy.desligar()
# galaxy.log_file_mixin.log_error('Desligou')

# HERANÇA
galaxy.ligar()
galaxy.desligar()
