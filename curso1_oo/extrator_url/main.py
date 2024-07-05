url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

# Sanitizando URL:
url = url.strip()
print(url)

# Validando URL:
if url == "":
    raise ValueError("URL Vazia")

# Separando base de parâmetros
posicao_caractere = url.find("?")
url_base = url[:posicao_caractere]
url_parametros = url[posicao_caractere + 1:]

# Obtendo valor do parâmetro
parametro_base = "quantidade"
indice_inicial_parametro_base = url_parametros.find(parametro_base) + len(parametro_base) + 1
indice_final_parametro_base = url_parametros.find("&", indice_inicial_parametro_base)

if indice_final_parametro_base == -1:
    valor_parametro = url_parametros[indice_inicial_parametro_base:]
else:
    valor_parametro = url_parametros[indice_inicial_parametro_base:indice_final_parametro_base]

print(valor_parametro)

# Desenvolvimento do código:
# for i in url:
#     if i == "?":
#         posicao_caractere = url.index(i)
# if posicao_caractere != -1:
#     print("A URL possui o caractere ?.")
# else:
#     print("A URL não possui o caractere ?.")

# posicao_final = len(url)
