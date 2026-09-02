class SaldoInsuficienteError(Exception):
    """Exceção lançada quando o saldo é insuficiente para realizar o saque."""
    pass

class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError(f"Saldo insuficiente! Saldo atual: R${self.saldo:.2f}, valor do saque: R${valor:.2f}")
        self.saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo restante: R${self.saldo:.2f}")

# Testando a conta bancária
conta = ContaBancaria(saldo_inicial=100.0)

try:
    conta.sacar(150.0)  # Tenta sacar mais do que possui
except SaldoInsuficienteError as e:
    print(f"Erro ao processar operação: {e}")