while True:
    print("\n=== MENU DE OPÇÕES ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção (1-3): ")
    
    if opcao == '1':
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print(f"Resultado da Soma: {n1 + n2}")
        
    elif opcao == '2':
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print(f"Resultado da Subtração: {n1 - n2}")
        
    elif opcao == '3':
        print("Encerrando o programa... Até logo!")
        break # Sai do laço de repetição
        
    else:
        print("Opção inválida! Tente novamente.")