import forca
import adivinhacao2


def escolhe_jogos():
    print("Escolha o seu jogo!")
    jogo = int(input("Digite 1 para Forca e 2 para Adivinhação: "))
    if jogo == 1:
        print("Forca")
        forca.jogar()
    elif jogo == 2:
        print("Adivinhação")
        adivinhacao2.jogar()
    else:
        print("Digite um número válido.")


if __name__ == "__main__":
    escolhe_jogos()
