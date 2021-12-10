from conta import conta

if __name__ == "__main__":
    conta1 = conta(322, "Willian Alves Fonseca", 250.00, 2000.00)
    conta2 = conta(222, "Willian Alves Fonseca", 5000.00, 10000.00)

    conta1.transferir(100, conta2)

    conta1.extrato()

    conta2.extrato()
