"""
REPOSITÓRIO: portfolio-academico
LOCALIZAÇÃO: fucapi/periodo2/paradigmas_lp/classe_retangulo.py
CONCEITOS: POO, Métodos Matemáticos, Atributos de Instância

ENUNCIADO:
    Crie uma classe Retangulo com: largura e altura.
    Implemente os métodos:
    - calcularArea(): Retorna largura * altura.
    - calcularPerimetro(): Retorna 2 * (largura + altura).
    Mostre os resultados no programa principal.
"""

class Retangulo: # Classe Retangulo
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self): # Método para calcular a área do retangulo
        return self.largura * self.altura

    def calcular_perimetro(self): # Método para calcular o perímetro do retangulo
        return 2 * (self.largura + self.altura)

def main():
    try: # Bloco Try Except para capturar erro
        print("--- Cálculos do Retângulo ---")
        l = float(input("Digite a largura: "))
        a = float(input("Digite a altura: "))

        # Criando o objeto retangulo
        meu_retangulo = Retangulo(l, a)

        # Executando os cálculos através dos métodos
        area = meu_retangulo.calcular_area()
        perimetro = meu_retangulo.calcular_perimetro()

        print(f"\nResultados para o Retângulo {l}x{a}:")
        print(f"Área: {area:.2f}")
        print(f"Perímetro: {perimetro:.2f}")

    except ValueError:
        # Mensagem de erro
        print("Erro: Por favor, insira valores numéricos para as dimensões.")

if __name__ == "__main__":
    main()
