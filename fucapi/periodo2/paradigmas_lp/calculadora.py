"""
REPOSITÓRIO: formacao-software-eng
LOCALIZAÇÃO: fucapi/periodo2/paradigmas_lp/calculadora.py
CONCEITOS: Estruturas Condicionais, Match Case, Operadores Aritméticos

ENUNCIADO:
    Leia dois números e uma operação (+, -, *, /). 
    Mostre o resultado da operação escolhida.
"""

def calcular():
  try: # Bloco Try Except para capturar erro
    # Entrada de dados
    num_1 = float(input("Digite o primeiro número: ")) # Input para num_1
    num_2 = float(input("Digite o segundo número: ")) # Input para num_2
    op_type = input("Digite a operação: ") # Input para select operação
    
    # Case para cada operação
    match op_type:
        case '+': # Soma
            resultado = num_1 + num_2
        case '-': # Subtração
            resultado = num_1 - num_2
        case '*': # Multiplicação
            resultado = num_1 * num_2
        case '/': # Divisão
                resultado = num_1 / num_2 if num_2 != 0 else "Erro: Divisão por zero não existe."
        case _: # Case default para operação vazia ou inválida 
            resultado = "Operação inválida."

    # Saída de dados
    print(f'Resultado: {resultado:.2f}')
    
  except ValueError:
    print("Erro, por favor insira apenas valores numéricos.") 

if __name__ == "__main__":
    calcular()
