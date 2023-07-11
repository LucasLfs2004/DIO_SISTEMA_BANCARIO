menu = """ 
###  Banco  ###

1. Depositar
2. Sacar
3. extrato
4. Sair
"""
saldo = 0
limite = 500
extrato = "\n##  Extrato  ##\n"
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        deposito = int(input("Qual a quantia que deseja depositar? "))
        saldo += deposito
        extrato += f"\nDepósito: R${deposito}"
    elif opcao == 2:
        saque = int(input("Qual a quantia que deseja sacar? "))
        if (numero_saques == LIMITE_SAQUES):
            print("Você excedeu o limite de saques diários")
        else:
            if (saque <= limite):
                saldo -= saque
                numero_saques += 1
                print("Saque realizado com sucesso")
                extrato += f"\nSaque: R${saque}"
            elif (saque > limite):
                print("O saque solicitado é maior do que o limite permitido para saques")
    elif opcao == 3:
        print(f"{extrato}\n\n## Saldo: R${saldo} ##")
    elif opcao == 4:
        print("Saindo!")
        break
    else:
        print("Opção inválida")
