"""
REPOSITÓRIO: portfolio-academico
LOCALIZAÇÃO: fucapi/periodo2/paradigmas_lp/tabuada.py
CONCEITOS: Laços de Repetição (For), Range, F-strings

ENUNCIADO:
    Faça um programa que:
    Leia um número inteiro;
    Mostre a tabuada desse número de 1 até 10.
"""

def gerar_tabuada():
    try: # Bloco Try Except para capturar erro
        # Entrada de dados
        numero = int(input("Digite um número inteiro para ver sua tabuada: "))
        
        print(f"\n--- Tabuada do {numero} ---")
        
        # O range(1, 11) vai de 1 até 10
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i:2} = {resultado}")
            
    except ValueError:
        #  Mensagem de erro
        print("Erro, por favor insira apenas valores numéricos.")

if __name__ == "__main__":
    gerar_tabuada()