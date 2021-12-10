# EXPLICAÇÃO DE COMO UTILIZAR OUTRA MANEIRA DE UTILIZAR A NOTAÇÃ GET/SET
class Cliente_explicacao:
    def __init__(self, nome) -> None:
        self.__nome = nome

    # criar um getter mais utilizando o nome do atributo da classe
    # Maneira bem comum de ser encontrado, e até mais pratico
    @property
    def nome(self):
        print("Chamamando @property do nome()")
        return self.__nome.Title()

    # criar um setter mais utilizando o nome do atributo da classe
    # Maneira bem comum de ser encontrado, e até mais pratico
    @nome.setter
    def nome(self, nome):
        print("Chamamando @setter nome()")
        self.__nome = nome
        print("Nome: {}".format(self.nome))


if __name__ == "__main__":
    cliente1 = Cliente_explicacao("Willian Alves Fonseca")

    cliente1.nome
    print("===============================")
    cliente1.nome = "Willian Roberto"
    print("===============================")
    cliente1.nome
    print("===============================")
