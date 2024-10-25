from abc import ABC, abstractmethod

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def exibir_saldo(self):
        print(f"Saldo atual de {self.titular}: R${self._saldo:.2f}")


class ServicoDeRelatorio:
    def gerar_relatorio(self, conta):
        print(f"Relatório - Titular: {conta.titular}, Saldo: R${conta._saldo:.2f}")


class Banco:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        print(f"Conta adicionada para {conta.titular}.")

    def buscar_conta(self, titular):
        for conta in self.contas:
            if conta.titular == titular:
                return conta
        print("Conta não encontrada.")
        return None


class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo=0, limite=500):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if 0 < valor <= (self._saldo + self.limite):
            self._saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor acima do limite.")


class Transacao(ABC):
    @abstractmethod
    def realizar(self, conta, valor):
        pass


class Deposito(Transacao):
    def realizar(self, conta, valor):
        conta.depositar(valor)


class Saque(Transacao):
    def realizar(self, conta, valor):
        conta.sacar(valor)


class ProcessadorDeTransacao:
    def __init__(self, transacao: Transacao):
        self.transacao = transacao

    def processar(self, conta, valor):
        self.transacao.realizar(conta, valor)


banco = Banco()
conta_alice = ContaCorrente("Alice")
banco.adicionar_conta(conta_alice)

transacao_deposito = ProcessadorDeTransacao(Deposito())
transacao_deposito.processar(conta_alice, 1000)

transacao_saque = ProcessadorDeTransacao(Saque())
transacao_saque.processar(conta_alice, 200)

relatorio = ServicoDeRelatorio()
relatorio.gerar_relatorio(conta_alice)
