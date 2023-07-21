
print ("=======> Bem Vindo ao Banco <========")

conta_normal = True

saldo = 450
saque = int(input("Digite o valor que quer sacar:"))

cheque_especial = 850

if conta_normal:

    if saque > (saldo and cheque_especial):
        print("Saldo insuficiente!")

    elif saque == cheque_especial:
        print("Saque realizado com cheque especial, confira as taxas!")

    else:
        print("Não foi possivél realizar o saque!")

