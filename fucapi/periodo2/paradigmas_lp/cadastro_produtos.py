"""
REPOSITÓRIO: portfolio-academico
LOCALIZAÇÃO: fucapi/periodo2/paradigmas_lp/cadastro_produtos.py
CONCEITOS: Listas (List), Laços de Repetição (For), Manipulação de Dados

ENUNCIADO:
    Crie um programa que:
    Permita cadastrar 5 produtos; 
    Armazene os nomes em uma lista; 
    Ao final, mostre todos os produtos cadastrados.
"""

def cadastrar_produtos():
    # Inicializando uma lista vazia
    lista_produtos = []

    print("--- Cadastro de Produtos ---")

    # Laço para repetir a entrada 5 vezes
    for i in range(1, 6):
        nome = input(f"Digite o nome do {i}º produto: ").strip()
        
        # Adicionando o nome à lista
        if nome:
            lista_produtos.append(nome) # Append adiciona no fim da lista
        else:
            print("Aviso: Nome vazio não foi adicionado.")

    # Saída de dados
    print("\n--- Produtos Cadastrados ---")
    if lista_produtos:
        for index, produto in enumerate(lista_produtos, start=1):
            print(f"{index}. {produto}")
    else:
        # Lista vazia
        print("Nenhum produto foi cadastrado.")

if __name__ == "__main__":
    cadastrar_produtos()