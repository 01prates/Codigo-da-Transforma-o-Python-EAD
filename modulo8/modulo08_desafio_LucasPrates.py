class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  # Status inicial do livro

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' - {self.autor} [{status}]"


class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.acervo = []  # Lista para guardar os objetos do tipo Livro

    def adicionar_livro(self, livro):
        self.acervo.append(livro)
        print(f"Livro '{livro.titulo}' adicionado com sucesso!")

    def emprestar_livro(self, titulo):
        for livro in self.acervo:
            if livro.titulo.lower() == titulo.lower():
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"Empréstimo realizado: '{livro.titulo}'")
                    return
                else:
                    print(f"O livro '{livro.titulo}' já está emprestado.")
                    return
        print(f"O livro '{titulo}' não foi encontrado na biblioteca.")

    def devolver_livro(self, titulo):
        for livro in self.acervo:
            if livro.titulo.lower() == titulo.lower():
                if not livro.disponivel:
                    livro.disponivel = True
                    print(f"Devolução realizada: '{livro.titulo}'")
                    return
                else:
                    print(f"O livro '{livro.titulo}' já está disponível no acervo.")
                    return
        print(f"O livro '{titulo}' não pertence a esta biblioteca.")

    def listar_livros(self):
        print(f"\n--- Livros na Biblioteca '{self.nome}' ---")
        if not self.acervo:
            print("Nenhum livro cadastrado.")
        for livro in self.acervo:
            print(livro)
        print("-------------------------------------------\n")


# --- Testando o Desafio Extra ---
if __name__ == "__main__":
    # Criando a biblioteca
    minha_biblioteca = Biblioteca("Biblioteca Comunitária")

    # Criando os livros
    livro1 = Livro("Dom Casmurro", "Machado de Assis")
    livro2 = Livro("1984", "George Orwell")

    # Adicionando livros ao acervo
    minha_biblioteca.adicionar_livro(livro1)
    minha_biblioteca.adicionar_livro(livro2)

    # Listando livros disponíveis
    minha_biblioteca.listar_livros()

    # Emprestando um livro
    minha_biblioteca.emprestar_livro("1984")
    minha_biblioteca.listar_livros()

    # Tentando emprestar novamente o mesmo livro
    minha_biblioteca.emprestar_livro("1984")

    # Devolvendo o livro
    minha_biblioteca.devolver_livro("1984")
    minha_biblioteca.listar_livros()