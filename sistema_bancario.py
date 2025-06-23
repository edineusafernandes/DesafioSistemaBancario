menu = """
    *** MENU ***
    Escolha uma opção:
    [d] Depósitar
    [e] Extrato
    [s] Sacar
    [0] Sair

    Digite a sua escolha: 
    
"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3

while True:
    mostrar_menu = input(menu)

    if mostrar_menu == 'd':
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("O valor informado está incorreto.")

    elif mostrar_menu == 'e':
        print("\n********** EXTRATO **********")
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n********************")

    elif mostrar_menu == 's':
        valor = float(input("Informe o valor que deseja sacar: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque >= limite_saque

        if excedeu_saldo:
            print("Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("O valor do saque excedeu o limite.")
        elif excedeu_saques:
            print("Você atingiu o número máximo de saques.")


        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}"
            numero_saque += 1

        else:
            print("O valor informado é invláido. Tente novamente.")

    elif mostrar_menu == '0':
        print("\n===== Obrigado por usar o nosso Banco =====")
        print("\nO sistema foi encerrado com sucesso. Até breve!")
        print("=============================================")
        break

else:
    print("Opção inválida. Por favor, selecione uma opção no MENU.")