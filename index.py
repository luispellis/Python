
from time import sleep

from click import clear

menu = """
    ---------------------------------------------

            BEM VINDO AO BANCO DIGITAL

        [1] Depositar [2] Saque [3] Extrato

    

    

                                     [0] Sair
    ---------------------------------------------
"""

saldo = 0
limite = 500
extrato = ""
numero_Saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = int(input(menu))
    clear()
    if opcao == 1 :
        print("""
            ---------------------------------------------

                            Deposito

            ---------------------------------------------                
        """)
        valorDeposito = float(input("\nQual o valor deseja depositar? "))

        if valorDeposito > 0:
            saldo += valorDeposito
            extrato += f"Deposito: R$ {valorDeposito:.2f}\n"
            sleep(2)
            clear()

        else:
            print("Valor inválido, tente novamente... ")
            sleep(2)
            clear()

    elif opcao == 2 :

        print("""
            ---------------------------------------------

                            SAQUE

            ---------------------------------------------
        """)
        valorSaque = float(input("Valor do saque? "))

        excedeu_saldo = valorSaque > saldo

        excedeu_limite = valorSaque > limite

        excedeu_saque = numero_Saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Valor indisponível, sem saldo!!!")
            sleep(2)
            clear()

        elif excedeu_limite:
            print("Excedeu o valor limite de saque R$ 500,00 ")
            sleep(2)
            clear()

        elif excedeu_saque:
            print("Você excedeu a quantidade de saques diário!!!")
            sleep(2)
            clear()

        elif valorSaque > 0:
            saldo -= valorSaque
            extrato += f"Saque: R$ {valorSaque:.2f}\n"
            numero_Saques += 1
            sleep(2)
            clear()

    elif opcao == 3 :
        print("""
            ------------------------------------------------

                                Extrato

            ------------------------------------------------    
        """)
        print("     Não teve movimentação na sua conta. \n" if not extrato else extrato)
        print(      f"Saldo: R$ {saldo:.2f}")
        print("     ------------------------------------------------")
        sleep(2)
        clear()

    elif opcao == 0 :
        break

    else:
        print("Opção Inválida!!! tente novamente ... ")
        sleep(2)
        clear()