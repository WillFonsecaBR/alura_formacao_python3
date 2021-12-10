

class conta:
    # ESTA FUNÇÃO CONTROI UM OBJETO
    def __init__(self, numero, titular, saldo, limite) -> None:
        # print("construindo um objeto ....{}".format(self))
        self.__numuro = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo += valor

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

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            print("o valor R${} foi sacado com sucesso!".format(valor))
            print("=================================")
        else:
            print(
                "o valor R${} não pode ser sacado, valor acima do limite!".format(valor))
            print("O saldo atual é de R${}".format(self.__saldo))
            print("=================================")

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        print("o valor R${} foi transferido com sucesso!".format(valor))
        print("=================================")

    # METODOS ESTATICOS (NÃO É USUAL ESTE TIPO DE IMPLEMENTAÇÃO)
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}


if __name__ == "__main__":
    conta1 = conta(322, "Will Fonseca", 250.00, 2000.00)
    conta2 = conta(222, "Willian Fonseca", 5000.00, 10000.00)

    conta1.transferir(100, conta2)

    conta1.extrato()

    conta2.extrato()

    conta1.limite = 2000
    conta1.saldo = 3000

    conta1.sacar(200000)

    conta1.extrato()
