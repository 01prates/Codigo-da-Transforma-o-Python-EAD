agenda = {}

while True:
    print("\n=== AGENDA DE CONTATOS ===")
    print("1. Adicionar Contato")
    print("2. Buscar Contato")
    print("3. Remover Contato")
    print("4. Listar Todos os Contatos")
    print("5. Sair")
    
    opcao = input("Escolha uma opção (1-5): ")
    
    if opcao == '1':
        nome = input("Digite o nome: ").strip()
        telefone = input("Digite o telefone: ").strip()
        agenda[nome] = telefone
        print(f"Contato '{nome}' adicionado/atualizado com sucesso!")
        
    elif opcao == '2':
        nome = input("Digite o nome para buscar: ").strip()
        if nome in agenda:
            print(f"📞 Telefone de {nome}: {agenda[nome]}")
        else:
            print(f"Contato '{nome}' não encontrado.")
            
    elif opcao == '3':
        nome = input("Digite o nome para remover: ").strip()
        if nome in agenda:
            del agenda[nome] # Remove a chave e valor correspondentes
            print(f"Contato '{nome}' removido com sucesso!")
        else:
            print(f"Contato '{nome}' não encontrado.")
            
    elif opcao == '4':
        if not agenda:
            print("A agenda está vazia!")
        else:
            print("\n--- Lista de Contatos ---")
            for nome, telefone in agenda.items():
                print(f"👤 {nome}: 📞 {telefone}")
                
    elif opcao == '5':
        print("Encerrando a agenda. Até mais!")
        break
    else:
        print("Opção inválida! Tente novamente.")