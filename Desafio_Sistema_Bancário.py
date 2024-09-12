menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite_saque_max = 500
extrato = ""
numero_saques = 0
qtd_limite_saques_dia = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_saque_max
        excedeu_saques = numero_saques >= qtd_limite_saques_dia

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")

        elif excedeu_limite:
            print(f"Operação falhou! Valor máximo permitido por saque é de: R$ {limite_saque_max}.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diario excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! Valor inválido.")

    elif opcao == "e":
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "q":
        print("Encerrando o sistema. Até logo!")
        break

    else:
        print("Operação inválida, selecione novamente uma operação desejada.")
