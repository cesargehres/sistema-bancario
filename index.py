#Deve ser possível depositar valores positivos para a minha conta bancária.
#Permitir realizar 3 saques diários com limite máximo de R$ 500 por saque.
#Caso o usuário não tenha saldo, exibir mensagem informando não ser possível sacar por falta de saldo.
#Extrato listandos todos os depósitos e saques.
#Se extrato estiver em branco exibir mensagem: Não foram realizadas movimentações.
#Valores devem ser exibidos utilizando o formato: R$ xxx.xx

menu = str("""Selecione uma operação:
-----------------------
[1] Saque
[2] Depósito
[3] Extrato
[4] Sair
-----------------------
""")

saldo = float(100)
limite_de_saques = int(3)
extrato = str("")

while True:
    operacao = int(input(menu))

    if (operacao == 1):
        if (limite_de_saques <= 0):
            print("Limite de saques excedido.\n")
            continue

        valor = float(input("Valor de Saque: R$ "))
        if (valor > saldo):
            print("Saldo insuficiente\n")
        elif (valor < 1):
            print("Valor mínimo de saque: R$ 1.00\n")
        elif (valor > 500):
            print("valor máximo de saque: R$ 500.00\n")
        else:
            saldo -= valor
            limite_de_saques -= 1
            extrato += str(f"- R$ {valor:.2f}\n")
            print("Saque concluído!\n")

    elif (operacao == 2):
        valor = float(input("Valor para depósito: R$ "))

        if (valor < 1):
            print("Valor mínimo para depósito: R$ 1.00\n")
        else:
            saldo += valor
            extrato += str(f"+ R$ {valor:.2f}\n")
            print("Dpósito concluído!\n")

    elif (operacao == 3):
        if extrato:
            print(f"Extrato:\n"
                  f"{extrato}"
                  f"Saldo: R$ {saldo:.2f}\n")
        else:
            print("Não foram realizadas movimentações.")

    elif (operacao == 4):
        break

    else:
        print("Erro! Digite uma operação válida!\n")
        continue