class CredenciaisInvalidasError(Exception):
    """Exceção para login ou senha incorretos."""
    pass

def sistema_login():
    usuario_correto = "lucas"
    senha_correta = "0000"
    tentativas_restantes = 3

    while tentativas_restantes > 0:
        try:
            user = input("Usuário: ")
            senha = input("Senha: ")

            if user != usuario_correto or senha != senha_correta:
                tentativas_restantes -= 1
                raise CredenciaisInvalidasError(f"Credenciais incorretas! Tentativas restantes: {tentativas_restantes}")

            print("Login realizado com sucesso!")
            return

        except CredenciaisInvalidasError as e:
            print(f"Erro: {e}\n")

    print("Acesso bloqueado: número máximo de tentativas excedido.")

sistema_login()