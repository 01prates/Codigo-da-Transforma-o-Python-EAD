lista_de_compras = []

while True:
    print("\n--- LISTA DE COMPRAS ---")
    print("1. Ver lista")
    print("2. Adicionar item")
    print("3. Remover item")
    print("4. Sair")
    
    opcao = input("Escolha uma opção (1-4): ")
    
    if opcao == '1':
        if not lista_de_compras:
            print("Sua lista está vazia!")
        else:
            print("\nItens na lista:")
            for i, item in enumerate(lista_de_compras, 1):
                print(f"{i}. {item}")
                
    elif opcao == '2':
        novo_item = input("Digite o nome do item a adicionar: ").strip()
        if novo_item:
            lista_de_compras.append(novo_item)
            print(f"'{novo_item}' foi adicionado à lista!")
            
    elif opcao == '3':
        item_remover = input("Digite o nome do item a remover: ").strip()
        if item_remover in lista_de_compras:
            lista_de_compras.remove(item_remover)
            print(f"'{item_remover}' foi removido!")
        else:
            print(f"O item '{item_remover}' não está na lista.")
            
    elif opcao == '4':
        print("Saindo da lista de compras. Boas compras!")
        break
    else:
        print("Opção inválida!")