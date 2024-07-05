print("Bem vindo ao jogo de advinhação!")
numero_secreto = 20
condicao = "s"
contador = 0
rodadas = 1
while condicao == "s":
    print("Tentativa {}".format(rodadas))
    chute = int(input("Digite um número: "))
    acerto = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if acerto:
        print("Você acertou")
        contador = 1
        break
    else:
        if maior:
            print("Você errou. O número que você chutou é maior que o número secreto.")
        elif menor:
            print("Você errou. O número que você chutou é menor que o número secreto.")
    condicao = input("Você gostaria de tentar novamente. Digite S para sim ou outro caracter para não: ")
    rodadas = rodadas + 1
if contador == 0:
    print('Você finalizou o jogo. O número correto é', numero_secreto)

