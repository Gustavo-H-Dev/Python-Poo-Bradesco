from Cliente import Cliente
from Conta import Conta


class Main:
    pass


c1 = Cliente("João", "04799775-2117")
conta = Conta(c1.get_nome(), 6565)

conta.deposita(100)
conta.saque(110)
conta.extrato()

