import random


def jogar():
    limite_inferior = 1
    limite_superior = 24

    # Gerando número secreto aleatório
    numero_secreto = random.randint(limite_inferior, limite_superior)

    # Definindo o número máximo de tentativas fixo
    max_tentativas = 6

    print("=== JOGO DA ADIVINHAÇÃO ===")
    print(
        f"Tente adivinhar o número entre {limite_inferior} e {limite_superior}."
    )
    print(f"Você tem {max_tentativas} tentativas!\n")

    tentativas = 0
    while tentativas < max_tentativas:
        palpite = int(
            input(f"Tentativa {tentativas + 1}: Digite seu palpite: ")
        )
        tentativas += 1

        if palpite == numero_secreto:
            print(
                f"Parabéns! Você acertou em {tentativas} tentativa(s)!"
            )
            break
        elif palpite < numero_secreto:
            print("O número secreto é MAIOR.")
        else:
            print("O número secreto é MENOR.")
    else:
        print(f"\nFim de jogo! O número era {numero_secreto}.")


if __name__ == "__main__":
    jogar()

while True:
    jogar()
    resposta = input("Deseja jogar novamente? (s/n): ")
    if resposta != "s":
        break
    else:
        print("\nReiniciando o jogo...\n")