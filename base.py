menu = """

[d] 💵 Depositar
[s] 💸 Sacar
[e] 🧾 Extrato
[q] 👋 Sair

=> """

limite = 500
saldo = 0
LIMITE_SAQUE = 3
numero_saques = 0
extrato = ""

while True:
    entry = input(menu)
    if entry == "d":
        value = float(input("Digite o valor do depósito: "))
        if value > 0:
            saldo += value
            extrato += f"Depósito: R$ {value:.2f}💰\n"
            print(f"✅ Depósito de R$ {value:.2f} realizado com sucesso!😁")
        else:
            print("❌ Operação falhou, digite um valor válido.")
    elif entry == "s":
        value = float(input("Digite o valor do saque: "))
        excedeu_limite = value > limite
        excedeu_saldo = value > saldo
        excedeu_quantidade_saque = numero_saques >= LIMITE_SAQUE
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print(f"Operação falhou! Limite de saque excedido você tem R$ {limite:.2f} por saque.")
        elif excedeu_quantidade_saque:
            print("Operação falhou! Limite diario de saque excedido.")
        elif value > 0:
            saldo -= value
            extrato += f"Saque: R$ {value:.2f}💸\n"
            numero_saques += 1
            print(f"✅ Saque de R${value:.2f} realizado com sucesso!💸")
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif entry == "e":
        print(f"\n{" EXTRATO BANCÁRIO ".center(40, "=")}\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}💰" if saldo > 0 else f"\nSaldo: R$ {saldo:.2f}😞")
        print("=" * 40)
    elif entry == "q":
        print("Tenha um excelente dia!🕊️🤝")
        break
    else:
        print("❌ Opção inválida, por favor digite a opção correta.")