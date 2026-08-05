# Dicionário global para armazenar os usuários cadastrados
# Formato: { "nome_usuario": "senha" }
usuarios_cadastrados = {}

def cadastrar_usuario():
    print("\n--- TELA DE CADASTRO ---")
    
    # 1. Validação do Nome de Usuário (único e não vazio)
    while True:
        usuario = input("Digite um nome de usuário: ").strip()
        if not usuario:
            print("❌ O nome de usuário não pode ficar em branco.")
        elif usuario in usuarios_cadastrados:
            print("❌ Este nome de usuário já está em uso! Escolha outro.")
        else:
            break

    # 2. Validação da Senha (4 a 6 caracteres e única)
    while True:
        senha = input("Digite uma senha (entre 4 e 6 caracteres): ").strip()
        
        if len(senha) < 4 or len(senha) > 6:
            print("❌ A senha deve ter entre 4 e 6 caracteres!")
        elif senha in usuarios_cadastrados.values():
            print("❌ Esta senha já está cadastrada por outro usuário! Escolha outra senha.")
        else:
            break
            
    # Salva no dicionário
    usuarios_cadastrados[usuario] = senha
    print(f"✅ Usuário '{usuario}' cadastrado com sucesso!")

def fazer_login():
    print("\n--- TELA DE LOGIN ---")
    if not usuarios_cadastrados:
        print("❌ Nenhum usuário cadastrado no sistema ainda! Cadastre-se primeiro.")
        return

    usuario = input("Usuário: ").strip()
    senha = input("Senha: ").strip()

    # Validação no dicionário
    if usuario in usuarios_cadastrados and usuarios_cadastrados[usuario] == senha:
        print(f"\n🎉 Login bem-sucedido! Bem-vindo(a), {usuario}!")
    else:
        print("\n❌ Falha no login! Usuário ou senha incorretos.")

# --- MENU PRINCIPAL DO SISTEMA ---
while True:
    print("\n=== SISTEMA DE ACESSO ===")
    print("1. Cadastrar")
    print("2. Login")
    print("3. Sair")
    
    opcao = input("Escolha uma opção (1-3): ").strip()
    
    if opcao == '1':
        cadastrar_usuario()
    elif opcao == '2':
        fazer_login()
    elif opcao == '3':
        print("Encerrando o sistema... Até mais!")
        break
    else:
        print("❌ Opção inválida! Escolha 1, 2 ou 3.")