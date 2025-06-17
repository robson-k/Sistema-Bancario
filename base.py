menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

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
            ...
    elif entry == "s":
        value = float(input("Digite o valor do saque: "))
        excedeu_limite = value > limite
        excedeu_saldo = value > saldo
        excedeu_quantidade_saque = numero_saques > LIMITE_SAQUE

        if value > 0:
            ...
    elif entry == "e":
        print(f"\n{" EXTRATO BANCÁRIO ".center(40, "=")}")

        print("=" * 40, end="")
    elif entry == "q":
        break
    else:
        print("Opção inválida, por favor digite a opção correta.")