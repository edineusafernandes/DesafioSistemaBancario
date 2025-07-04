import textwrap

def menu():
    menu ="""
    *** MENU ***
    Escolha uma opção:
    [d] Depósitar
    [e] Extrato
    [s] Sacar
    [n] Nova conta
    [l] Listar contas
    [u] Novo usuário
    [0] Sair

    Digite a sua escolha: 
    
"""
    return input(textwrap.dedent(menu))

def depositar(salfo, valor, extrato):
        if valor > 0:
           saldo += valor
           extrato += f"Depósito: R$ {valor:.2f}\n"
           print("Depósito realizado com sucesso!")        
        else:
            print("O valor informado está incorreto.")

        return saldo, extrato

def sacar (*, saldo, valor, extrato, limite, numero_saque, limite_saque):
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
            print("Saque realizado com sucesso!")

        else:
            print("O valor informado é invláido. Tente novamente.")

        return saldo, extrato

def exibir_extrato(saldo, /, extrato):
        print("\n********** EXTRATO **********")
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n********************")

def criar_usuario(usuarios):
     cpf = input("Informe o CPF (somente números): ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
          print("Há um usuário cadastrado com esse CPF.")
          return

     nome = input("Informe nome e um sobrenome: ")
     data_nascimento = input("Informe a data de nascimento (dd/mm/aa): ")
     endereco = input("Informe o endereço (logradouro, número, bairro, cidade/sigla do Estado): ")

     usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
     print("Usuário cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agendia, numero_conta, usuarios):
     cpf = input("Digite o CPF do usuário: ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
          print("Conta de usuário criada com sucesso!")
          return {"agencia": agencia, "numero_conta": numero_conta, "usuacio": usuario}
     
     print("Usuário não cadastrado.")

def listar_contas(contas):
     for conta in contas:
          linha = f"""
            Agência: {conta['agencia']}
            Número da conta: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
            """
          print(">0<" * 50)
          print(textwrap.dedent(linha))

def main():
     
    saldo = 0
    limite = 500
    extrato = ""
    numero_saque = 0
    limite_saque = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    
while True:
    mostrar_menu = menu()

    if mostrar_menu == 'd':
        valor = float(input("Informe o valor do depósito: "))
                      
        saldo, extrato = depositar(saldo, extrato, valor)


    elif mostrar_menu == 'e':
         exibir_extrato(saldo, extrato = extrato)

    elif mostrar_menu == 'n':
         numero_conta = len(contas) +1
         conta = criar_conta(AGENCIA, numero_conta, usuarios)
         if conta:
              contas.append(conta) 

         elif mostrar_menu == 'l':
              listar_contas(contas)

         elif mostrar_menu == 'u':
              criar_usuario(usuarios)
     

    elif mostrar_menu == 's':
        valor = float(input("Informe o valor que deseja sacar: "))

        saldo,extrato = sacar(
            saldo = saldo,
            valor = valor,
            extrato = extrato,
            limite = limite,
            numero_saque = numero_saque,
            limite_saque = limite_saque,
        )
 

    elif mostrar_menu == '0':
        print("\n===== Obrigado por usar o nosso Banco =====")
        print("\nO sistema foi encerrado com sucesso. Até breve!")
        print("=============================================")
        break

else:
    print("Opção inválida. Por favor, selecione uma opção no MENU.")

main()
