print('Bem vindo ao banco X ')

menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 3
LIMITE_SAQUE = 3
msg = 'Por favor, digite um valor valido!!! '

while True:

    opcao = input(menu)

# Opção Deposito
    
    if opcao == "d":
        try:
            valor_deposito = input("Quanto gostaria de depositar: ")
            valor_float = float(valor_deposito)    

            saldo = valor_float + saldo

            print(f'Seu saldo é de RS {saldo:.2f}')
        except:
            print(msg)

# Opção Saque
            
    elif opcao == "s":
        
        try:
            valor_saque = input("Quanto gostaria de sacar: ")
            saque_float = float(valor_saque)

            nao_te_saldo = saque_float > saldo
            passou_limite = saque_float > limite
            passou_saque = numero_saques == 0

            if nao_te_saldo:
                print("Não foi possivel completar sua solicitação")
                print(f"valor indisponivel, voce tem um total de {saldo:.2f}." )

            elif passou_limite:
                print("Sinto muito, seu limite acabou! ")

            elif passou_saque:
                print("Sinto muito, seu limite de saque foi ultrapassado,")
                print("tente novamente mais tarde! ")        

            else:
                saldo = saldo - saque_float
                print(f"Seu saldo atual é {saldo:.2f}")
                numero_saques = numero_saques - 1


        except:
            print(msg)

# Opção Extrato
            
    elif opcao == "e":
        print(10 * '*' + " extrato " + 10* '*')
        print(f'Foi depositado o valor de R$ {saldo} em sua conta')
    
# Sair
        
    elif opcao == "q":
        break
    
    else:
        print(msg)



