"""
REPOSITÓRIO: portfolio-academico
LOCALIZAÇÃO: fucapi/periodo2/paradigmas_lp/sistema_biblioteca.py
CONCEITOS: POO, Composição de Objetos, Manipulação de Listas de Objetos

ENUNCIADO:
    Crie um sistema com duas classes:
    1. Livro: título, autor e disponibilidade. Método mostrarLivro().
    2. Biblioteca: lista de livros. Métodos adicionarLivro() e listarLivros().
"""

class Livro: # Classe livro
    def __init__(self, titulo, autor, disponível=True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponível

    def mostrar_livro(self): # Método para mostrar livro
        status = "Disponível" if self.disponivel else "Emprestado"
        print(f"Título: {self.titulo:20} | Autor: {self.autor:15} | Status: {status}")


class Biblioteca: # Classe biblioteca
    def __init__(self):
        # A biblioteca possui uma lista que armazenará objetos do tipo Livro
        self.livros = []

    def adicionar_livro(self, livro): # Método para adicionar livro
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado com sucesso!")

    def listar_livros(self): # Método para listar livros
        print("\n" + "="*60)
        print(f"{'CATÁLOGO DA BIBLIOTECA':^60}")
        print("="*60)
        if not self.livros:
            print("A biblioteca está vazia.")
        else:
            for livro in self.livros:
                livro.mostrar_livro()
        print("="*60)


def main():
    # Instanciando a Biblioteca
    minha_biblioteca = Biblioteca()

    # Criando objetos da classe Livro
    livro1 = Livro("Dom Casmurro", "Machado de Assis")
    livro2 = Livro("O Alquimista", "Paulo Coelho", disponível=False)
    livro3 = Livro("O Beijo da Neve", "Babi A. Sette")

    # Adicionando os livros à biblioteca
    minha_biblioteca.adicionar_livro(livro1)
    minha_biblioteca.adicionar_livro(livro2)
    minha_biblioteca.adicionar_livro(livro3)

    # Listando todos os livros cadastrados
    minha_biblioteca.listar_livros()

if __name__ == "__main__":
    main()
