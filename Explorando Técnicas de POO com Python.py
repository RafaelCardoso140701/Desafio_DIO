#1 / 2 - Criando Classes para Dados de Vendas
# Descrição
# Você está desenvolvendo um sistema para gerenciar dados de vendas que serão posteriormente importados para o Power BI. Você tem a estrutura de duas classes, Venda e Relatorio, já definidas. Sua tarefa é implementar partes específicas do código dentro dessas classes.

# Classe Venda:
# Já está definida e contém as informações sobre uma venda, como produto, quantidade e valor.

# Classe Relatorio:
# Você precisa implementar o método adicionar_venda, que deve verificar se o objeto passado é uma instância da classe Venda antes de adicioná-lo à lista de vendas.
# Também, no método calcular_total_vendas, você deve calcular o total de vendas multiplicando a quantidade pelo valor de cada venda adicionada ao relatório.

# Função main:
# Você deverá implementar a lógica para exibir o total de vendas utilizando o método calcular_total_vendas da classe Relatorio.

# Entrada
# A entrada consiste em dados de vendas com as seguintes colunas:
# Produto (string)
# Quantidade (inteiro)
# Valor (decimal)
# Saída
# A saída é o total de vendas calculado pela classe Relatorio.
class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Relatorio:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        # Verifica se o objeto passado é uma instância da classe Venda
        if isinstance(venda, Venda):
            self.vendas.append(venda)
        else:
            raise TypeError("O objeto passado não é uma instância da classe Venda")

    def calcular_total_vendas(self):
        total = 0
        for venda in self.vendas:
            # Calcula o total de vendas multiplicando a quantidade pelo valor
            total += venda.quantidade * venda.valor
        return total

def main():
    relatorio = Relatorio()
    
    print("")
    
    for _ in range(3):
        produto = input().strip()  # Lê o nome do produto
        quantidade = int(input().strip())  # Lê a quantidade e converte para inteiro
        valor = float(input().strip())  # Lê o valor e converte para float
        venda = Venda(produto, quantidade, valor)
        relatorio.adicionar_venda(venda)
    
    # Exibe o total de vendas usando o método calcular_total_vendas
    total_vendas = relatorio.calcular_total_vendas()
    print(f"Total de Vendas: {total_vendas:.1f}")

if __name__ == "__main__":
    main()

#2 / 2 - Agrupamento de Vendas por Categoria
#Descrição
# Você está desenvolvendo um sistema para organizar vendas por categorias antes de gerar um relatório. O objetivo é criar uma classe Categoria que gerencie as vendas associadas a uma determinada categoria e calcule o total de vendas dessa categoria.

# Tarefas:

# Método adicionar_venda: Na classe Categoria, crie um método chamado adicionar_venda que adiciona um objeto Venda à lista de vendas da categoria.

# Método total_vendas: Na classe Categoria, crie um método chamado total_vendas que calcula e retorna o total das vendas (soma do valor de todas as vendas) para essa categoria.

# Na função main:

# Entrada de Dados:

# Leia o nome das categorias e, para cada categoria, leia as vendas associadas.

# Implementação: Adicione cada venda à categoria correspondente usando o método adicionar_venda.

# Exibição dos Resultados:

# Exiba o total de vendas para cada categoria.

# Implementação: Utilize o método total_vendas para calcular e exibir o total das vendas.

# Entrada
# A entrada consiste em:

# Nome da Categoria (string)

# Lista de Vendas (com as colunas Produto, Quantidade, Valor)
# Saída
# A saída é o total de vendas por categoria.

class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []

    def adicionar_venda(self, venda):
        self.vendas.append(venda)

    def total_vendas(self):
        total = sum(venda.valor for venda in self.vendas)
        return total

def main():
    categorias = []

    for i in range(2):
        nome_categoria = input().strip()
        categoria = Categoria(nome_categoria)

        for j in range(2): 
            entrada_venda = input().strip()
            produto, quantidade, valor = entrada_venda.split(',')
            quantidade = int(quantidade.strip())
            valor = float(valor.strip())

            venda = Venda(produto.strip(), quantidade, valor)
            categoria.adicionar_venda(venda)

        categorias.append(categoria)
    
    # Exibindo os totais de vendas para cada categoria
    for categoria in categorias:
        total = categoria.total_vendas()
        print(f'Vendas em {categoria.nome}: {total:.1f}')

if __name__ == "__main__":
    main()
