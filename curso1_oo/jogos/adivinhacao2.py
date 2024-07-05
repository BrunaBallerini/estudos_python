import random


def jogar():
    print("Bem vindo ao jogo de advinhação!")
    numero_secreto = random.randrange(1, 101)
    contador = 0
    rodadas = 1
    total_tentativas = 0
    pontos = 1000

    print(numero_secreto)

    print("Qual nível de dificuldade você quer jogar?")
    dificuldade = input("Digite f para fácil, m para médio e d para difícil: ")
    if dificuldade == "f" or dificuldade == "F":
        total_tentativas = 10
    elif dificuldade == "m" or dificuldade == "M":
        total_tentativas = 5
    elif dificuldade == "d" or dificuldade == "D":
        total_tentativas = 3
    else:
        print("Você digitou um valor inválido. Você tem uma tentativa para o jogo.")
        total_tentativas = 1

    for rodadas in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodadas, total_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        acerto = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        limitante = chute < 1 or chute > 100
        if limitante:
            print("Valor inválido.")
            continue
        elif acerto:
            print("Você acertou. E o seus pontos são {}".format(pontos))
            contador = 1
            break
        else:
            if maior:
                print("Você errou. O número que você chutou é maior que o número secreto.")
                # pontos = pontos - (chute - numero_secreto)
            elif menor:
                print("Você errou. O número que você chutou é menor que o número secreto.")
                # pontos = pontos - (numero_secreto - chute)
            pontos = pontos - abs(numero_secreto - chute)

    if contador == 0:
        print("O jogo terminou. O número correto é {} e os seus pontos são {}.".format(numero_secreto, pontos))


if __name__ == "__main__":
    jogar()
