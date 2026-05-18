"""
REPOSITÓRIO: portfolio-academico
LOCALIZAÇÃO: fucapi/periodo2/paradigmas_lp/media_aluno.py
CONCEITOS: Entrada de Dados, Operadores Aritméticos, Match Case com Guards (if)

ENUNCIADO:
    Leia 3 notas de um aluno e calcule a média.
    Informe:
    - "Aprovado", se média >= 7;
    - "Recuperação", se média entre 5 e 6.9;
    - "Reprovado", se média < 5.
"""

def calcular_media():
    try: # Bloco Try Except para capturar erro
        # Entrada de dados
        n1 = float(input("Digite a primeira nota: ")) # Input para n1
        n2 = float(input("Digite a segunda nota: ")) # Input para n2
        n3 = float(input("Digite a terceira nota: ")) # Input para n3

        # Calculo para média
        media = (n1 + n2 + n3) / 3

        # Match case para selecionar cada caso
        match media:
            case m if m >= 7:
                situacao = "Aprovado"
            case m if 5 <= m < 7:
                situacao = "Recuperação"
            case _:
                situacao = "Reprovado"

        # Saída de dados
        print(f"\nMédia: {media:.2f}")
        print(f"Situação: {situacao}")

    except ValueError:
        # Mensagem de erro
        print("Erro: Insira apenas valores numéricos válidos para as notas.")

if __name__ == "__main__":
    calcular_media()
