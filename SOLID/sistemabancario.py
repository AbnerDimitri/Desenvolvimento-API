class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def exibir_saldo(self):
        print(f"Saldo atual de {self.titular}: R${self.saldo:.2f}")


class Banco:
    def __init__(self):
        self.contas = []

    def criar_conta(self, titular):
        conta = ContaBancaria(titular)
        self.contas.append(conta)
        print(f"Conta criada para {titular}.")

    def buscar_conta(self, titular):
        for conta in self.contas:
            if conta.titular == titular:
                return conta
        print("Conta não encontrada.")
        return None


banco = Banco()
banco.criar_conta("Alice")
conta_alice = banco.buscar_conta("Alice")

if conta_alice:
    conta_alice.depositar(1000)
    conta_alice.sacar(200)
    conta_alice.exibir_saldo()

banco.criar_conta("Bob")
conta_bob = banco.buscar_conta("Bob")

if conta_bob:
    conta_bob.depositar(500)
    conta_bob.sacar(600)  
    conta_bob.exibir_saldo()
