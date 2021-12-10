

class conta:
    # ESTA FUNÇÃO CONTROI UM OBJETO
    def __init__(self, numero, titular, saldo, limite) -> None:
        # print("construindo um objeto ....{}".format(self))
        self.__numuro = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def get_limite(self):
        return self.__limite

    def set_limite(self, valor):
        self.__limite = valor

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        self.__saldo == valor

    def extrato(self):
        print("Cliente: {}".format(self.__titular))
        print("Conta: {}".format(self.__numuro))
        print("saldo: R${}".format(self.__saldo))
        print("Limite: R${}".format(self.__limite))
        print("=================================")

    def depositar(self, valor):
        self.__saldo += valor
        print("o valor R${} foi depositado com sucesso!".format(valor))
        print("=================================")

    def sacar(self, valor):
        self.__saldo -= valor
        print("o valor R${} foi sacado com sucesso!".format(valor))
        print("=================================")

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        print("o valor R${} foi transferido com sucesso!".format(valor))
        print("=================================")


if __name__ == "__main__":
    conta1 = conta(322, "Willian Alves Fonseca", 250.00, 2000.00)
    conta2 = conta(222, "Willian Alves Fonseca", 5000.00, 10000.00)

    conta1.transferir(100, conta2)

    conta1.extrato()

    conta2.extrato()
