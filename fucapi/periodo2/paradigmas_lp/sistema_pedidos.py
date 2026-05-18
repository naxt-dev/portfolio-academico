"""
REPOSITÓRIO: portfolio-academico
LOCALIZAÇÃO: fucapi/periodo2/paradigmas_lp/sistema_pedidos.py
CONCEITOS: POO, Agregação de Objetos, Acumuladores e Formatação de Moeda

ENUNCIADO:
    Crie um sistema com duas classes:
    1. Produto: nome e preço. Método mostrarProduto().
    2. Pedido: lista de produtos. Métodos adicionarProduto(), 
       calcularTotal() e listarPedido().
    No programa principal, crie 3 produtos, adicione ao pedido e mostre o total.
"""

class Produto: # Classe produto
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar_produto(self): # Método para mostrar produto
        print(f"Produto: {self.nome:20} | Preço: R$ {self.preco:>8.2f}")


class Pedido: # Classe pedido
    def __init__(self):
        # O pedido agrega múltiplos objetos da classe Produto
        self.produtos = []

    def adicionar_produto(self, produto): # Método para adicionar produto
        self.produtos.append(produto)
        print(f"✓ {produto.nome} adicionado ao pedido.")

    def calcular_total(self): # Método para calcular preço dos produtos
        return sum(p.preco for p in self.produtos)

    def listar_pedido(self): # Método para listar pedidos
        print("\n" + "-"*45)
        print(f"{'RESUMO DO PEDIDO':^45}")
        print("-"*45)
        if not self.produtos:
            print("O pedido está vazio.")
        else:
            for p in self.produtos:
                p.mostrar_produto()
        print("-"*45)


def main():
    # Instanciando os produtos
    p1 = Produto("Teclado Mecânico", 250.00)
    p2 = Produto("Mouse Gamer", 180.00)
    p3 = Produto("Mousepad Extra Large", 85.50)
    
    # Criando o pedido
    meu_pedido = Pedido()
    
    # Adicionando produtos ao pedido
    print("Iniciando compra...")
    meu_pedido.adicionar_produto(p1)
    meu_pedido.adicionar_produto(p2)
    meu_pedido.adicionar_produto(p3)
    
    # Saída de dados (Listagem e total do pedido)
    meu_pedido.listar_pedido()
    total = meu_pedido.calcular_total()
    print(f"TOTAL DA COMPRA: R$ {total:>27.2f}")
    print("-"*45)

if __name__ == "__main__":
    main()
