import re


class ExtratorUrl:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    @staticmethod
    def sanitiza_url(url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:  # if self.url == "": => if not bool(self.url)
            raise ValueError("URL vazia.")

        padrao = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        verifica = padrao.match(self.url)
        if not verifica:
            raise ValueError("URL não válida.")

    def get_url_base(self):
        posicao_caractere = self.url.find("?")
        url_base = self.url[:posicao_caractere]
        return url_base

    def get_url_parametros(self):
        posicao_caractere = self.url.find("?")
        url_parametros = self.url[posicao_caractere + 1:]
        return url_parametros

    def obtem_valor_parametro(self, parametro_base):
        indice_inicial_parametro_base = self.get_url_parametros().find(parametro_base) + len(parametro_base) + 1
        indice_final_parametro_base = self.get_url_parametros().find("&", indice_inicial_parametro_base)

        if indice_final_parametro_base == -1:
            valor_parametro = self.get_url_parametros()[indice_inicial_parametro_base:]
        else:
            valor_parametro = self.get_url_parametros()[indice_inicial_parametro_base:indice_final_parametro_base]

        return valor_parametro

    # Tentativa Desafio
    # def calculo_cotacao(self, cotacao):
    #     return int(self.obtem_valor_parametro("quantidade")) * cotacao

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return "URL:{}\nURL Base:{}\nURL Parâmetros:{}".format(self.url, self.get_url_base(), self.get_url_parametros())

    def __eq__(self, other):
        return self.url == other.url


url_final = ExtratorUrl("https://bytebank.com/cambio?moedaOrigem=dolar&moedaDestino=real&quantidade=100")

# Aplicação método __len__
print("A URL tem {} caracteres.".format(len(url_final)))

# Aplicação método __str__
print(url_final)

# Aplicação do método __eq__
# url_comparacao = ExtratorUrl("https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
# print(url_final == url_comparacao)

# Tentativa Desafio
# valor_cotacao = url_final.calculo_cotacao(5.5)

# Desafio
moeda_origem = url_final.obtem_valor_parametro("moedaOrigem")
moeda_destino = url_final.obtem_valor_parametro("moedaDestino")
quantidade = url_final.obtem_valor_parametro("quantidade")
valor_dolar = 5.50

if moeda_origem == "real" and moeda_destino == "dolar":
    valor_conversao = int(quantidade) / valor_dolar
    print("O valor de R$" + quantidade + " reais é igual a $" + str(valor_conversao) + " dólares.")
elif moeda_origem == "dolar" and moeda_destino == "real":
    valor_conversao = int(quantidade) * valor_dolar
    print("O valor de $" + quantidade + " dólares é igual a R$" + str(valor_conversao) + " reais.")
else:
    print(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")
