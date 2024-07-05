import re

url = "https://bytebank.com.br/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
padrao = re.compile("(http(s)?://)(www.)?bytebank.com(.br)?/cambio")
verifica = padrao.match(url)
if not verifica:
    print("URL não válida")
else:
    print("URL é válida")

# Desenvolvimento do código
# posicao_caractere = self.url.find("?")
# url_base = self.url[:posicao_caractere]
# if not url_base.startswith("https") or not url_base.endswith("/cambio"):
#     print("URL com formato errado")
