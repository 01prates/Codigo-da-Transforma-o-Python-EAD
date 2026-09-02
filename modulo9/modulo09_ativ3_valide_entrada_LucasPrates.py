def cadastrar_usuario():
    while True:
        try:
            idade = int(input("Digite a sua idade: "))
            if idade <= 0:
                raise ValueError("A idade deve ser um número positivo (maior que zero).")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Tente novamente.")

    print(f"Idade cadastrada com sucesso: {idade} anos.")

cadastrar_usuario()