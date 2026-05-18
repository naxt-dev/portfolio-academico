"""
REPOSITÓRIO: portfolio-academico
LOCALIZAÇÃO: fucapi/periodo2/paradigmas_lp/classe_pessoa.py
CONCEITOS: Programação Orientada a Objetos (POO), Classes, Atributos e Métodos

ENUNCIADO:
    Crie uma classe chamada Pessoa com: atributos nome e idade.
    Crie um método chamado apresentar() que mostre as informações.
    No programa principal: crie um objeto, peça os dados pelo teclado 
    e chame o método.
"""

class Pessoa:
    # O método __init__ é o construtor que inicializa os atributos
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self): # Def de método para apresentar nome e idade
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

def main():
    try:
        # Entrada de dados
        nome_input = input("Digite o seu nome: ").strip() # Strip para remover espaço errado
        idade_input = int(input("Digite a sua idade: "))

        # Instanciando o objeto (Criando a "Pessoa")
        usuario = Pessoa(nome_input, idade_input)

        # Chamando o método do objeto criado
        print() # Apenas para pular uma linha
        usuario.apresentar()

    except ValueError:
        # Mensagem de erro
        print("Erro, A idade precisa ser um número inteiro.")

if __name__ == "__main__":
    main()