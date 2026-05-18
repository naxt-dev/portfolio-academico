"""
REPOSITÓRIO: formacao-software-eng
LOCALIZAÇÃO: fucapi/periodo2/paradigmas_lp/par_ou_impar.py
CONCEITOS: Operadores Aritméticos (Módulo), Estruturas Condicionais (Match Case)

ENUNCIADO:
    Faça um programa que:
    Leia um número inteiro; 
    Informe se ele é par ou ímpar.
"""

def verificar_paridade():
    try: # Bloco Try Except para capturar erro
        # Entrada de dados
        num = int(input("Digite um número inteiro: "))

        """
        Calculo para saber se o número é impar
        if num % 2 == 0 (Resto da divisão por 2 == 0), o número é par
        else (Resto da divisão qualquer valor além de 0), o número é ímpar
        """
        resultado = 'Par' if num % 2 == 0 else 'Ímpar'

        # Saída de dados
        print(f'Resultado: O número {num} é {resultado}.')

    except ValueError:
        # Mensagem de erro
        print("Erro, por favor insira apenas valores numéricos.")

if __name__ == '__main__':
    verificar_paridade()
