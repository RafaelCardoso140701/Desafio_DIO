from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.executar(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(nome, cpf, endereco)
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def criar_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor > self.saldo:
            print("Operação falhou! Saldo insuficiente.")
            return False
        if valor <= 0:
            print("Operação falhou! Valor inválido.")
            return False
        self._saldo -= valor
        print("Saque realizado com sucesso!")
        return True

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
            return True
        print("Operação falhou! Valor inválido.")
        return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite_saque_max=500, limite_saques_diario=3):
        super().__init__(numero, cliente)
        self.limite_saque_max = limite_saque_max
        self.limite_saques_diario = limite_saques_diario

    def sacar(self, valor):
        numero_saques = len([t for t in self.historico.transacoes if t["tipo"] == Saque.__name__])

        if valor > self.limite_saque_max:
            print("Operação falhou! Valor do saque excede o limite.")
            return False
        if numero_saques >= self.limite_saques_diario:
            print("Operação falhou! Número máximo de saques diário excedido.")
            return False
        return super().sacar(valor)

    def __str__(self):
        return f"""
            Agência:\t{self.agencia}
            Conta:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        })

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def executar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def executar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def executar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)

def menu():
    return """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [lu] Listar usuários
    [q] Sair
    => """

def filtrar_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta.")
        return None
    return cliente.contas[0]

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado.")
        return

    try:
        valor = float(input("Informe o valor do depósito: "))
    except ValueError:
        print("Valor inválido.")
        return

    transacao = Deposito(valor)
    conta = recuperar_conta_cliente(cliente)
    if conta:
        cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado.")
        return

    try:
        valor = float(input("Informe o valor do saque: "))
    except ValueError:
        print("Valor inválido.")
        return

    transacao = Saque(valor)
    conta = recuperar_conta_cliente(cliente)
    if conta:
        cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado.")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return


    transacoes = conta.historico.transacoes
    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in transacoes:
            print(f"{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}")
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Já existe cliente com esse CPF.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço: ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    print("Cliente criado com sucesso!")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado.")
        return

    conta = ContaCorrente.criar_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.adicionar_conta(conta)
    print("Conta criada com sucesso!")

def listar_contas(contas):
    if not contas:
        print("Não há contas cadastradas.")
        return

    for conta in contas:
        print("=" * 100)
        print(str(conta))

def listar_usuarios(clientes):
    if not clientes:
        print("Não existem usuários cadastrados.")
        return

    for cliente in clientes:
        print(f"Nome:\t\t{cliente.nome}")
        print(f"CPF:\t\t{cliente.cpf}")
        print(f"Data de Nascimento:\t{cliente.data_nascimento}")
        print(f"Endereço:\t{cliente.endereco}")
        print("=" * 100)

def main():
    clientes = []
    contas = []

    while True:
        opcao = input(menu()).strip().lower()

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "lu":
            listar_usuarios(clientes)
        elif opcao == "q":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Operação inválida. Selecione novamente uma operação.")

if __name__ == "__main__":
    main()
