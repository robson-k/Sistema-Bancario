"=============================== Pontos para se realizar atualização do Desafio Sistema Bancário da DIO ================================="
# Separar as funções existentes Depósito, Saque e Extrato e criar duas novas funções cadastrar usuário (cliente do banco) e cadastrar conta bancária (vincular cliente a conta).

# Criar usuário (cliente) - armazenar os usuários em uma lista um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado. Armazenar somente os números do cpf sem pontos e hífen. Não pode cadastrar 2 usuários com o mesmo CPF.
# Criar conta corrente - armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agencia é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
# Dica - para vincular um usuário a uma conta, filtrar a lista de usuários buscando o número do CPF informado para cada usuário da lista.

# Saque - receber argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.
# Depósito - receber argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.
# Extrato - receber argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.
# Criar duas novas funções: criar usuário e criar conta corrente. Se quiser adicionar mais funções pode, exemplo: listar contas.
"========================================================================================================================================"

menu = """

[ d ]  💵 Depositar
[ s ]  💸 Sacar
[ e ]  🧾 Extrato
[nu ]  🆕👤 Novo Usuário
[nc ]  ➕👤 Nova Conta
[ q ]  👋 Sair

=> """

AGENCIA = "0001"
LIMITE_SAQUE = 3


def apagar_terminal():
    from os import system, name

    system("cls" if name == "nt" else "clear")


def novo_usuario(usuarios): # Cadastro do usuário

    "================================================== Validação do nome do usuário ===================================================="
    while True: # Loop de verificação para ver se o nome e alfabetico.
        name = input("Nome: ").strip()
        
        if name.isalpha(): # Se não ele vai continuar pedindo o nome.
            break
    "===================================================================================================================================="


    print("-" * 40)

    "===================================================== 'Validação' data de nascimento ==============================================="
    print("Formato: (dd/mm/ano) ou (dd-mm-ano)")
    while True:
        nascimento = input("Nascimento: ").strip()
        if nascimento.count("/") == 2 or nascimento.count("-") == 2: # Verifica se dentro da entrada do usuário tem 2 -> "/" ou "-". 

            if "-" in nascimento and " " not in nascimento:
                dia, mes, ano = map(int, nascimento.split("-"))
                if 0 < dia <= 31 and 0 < mes <= 12 and 1000 < ano <= 2007: # Aqui a verificação é até 2007 para confirmar que a pessoa tem 18 anos pelo menos na verificação do ano de nascimento
                    nascimento_formatado = f"{dia:02}/{mes:02}/{ano}"
                    break
                else:
                    continue
            elif "/" in nascimento and " " not in nascimento:
                dia, mes, ano = map(int, nascimento.split("/"))
                if 0 < dia <= 31 and 0 < mes <= 12 and 1000 < ano <= 2007: # Aqui a verificação é até 2007 para confirmar que a pessoa tem 18 anos pelo menos na verificação do ano de nascimento
                    nascimento_formatado = f"{dia:02}/{mes:02}/{ano}"
                    break
                else: # Se não passar na verificação anterior vai continuar pedindo a data de nascimento.
                    continue
            else: # Caso não tenha dentro de nascimento nem "/" nem "-" ele vai continuar pedindo a data em um dos formatos corretos.
                continue

        else: # Caso o primeiro if não seja a entrada do usuário vai continuar o loop.
            continue
    "===================================================================================================================================="

    print("-" * 40)

    "========================================================= 'Validação' CPF =========================================================="
    while True: # Loop de verficação para validar o cpf
        cpf = input("CPF: (Somente números) ").strip()
        
        # Verifica se o cpf contém apenas núemros e se contem exatemaente 11 digitos
        if not (cpf.isdigit() and len(cpf) == 11):
            print("❌ CPF inválido! Deve conter exatamente 11 números.")
            continue

        # Verifica se o cpf já está cadastrado
        cpf_existente = any(user["CPF"] == cpf for user in usuarios)
        if cpf_existente:
            print("❌ Já existe um usuário com esse CPF. Cadastro cancelado!")
            return usuarios
        
        break # CPF válido e único, prossegue com o cadastro
    "===================================================================================================================================="
    
    print("-" * 130)    
    "======================================================== 'Validação' Endereço ======================================================"
    while True: # Loop de verificação para 'validar' endereço
        endereco = input("logradouro, nro - bairro - cidade/sigla estado -> ").strip()
        partes = endereco.split("-") # Faz a separação da variavel endereco por "-" retornando assim em uma unica variavel que vai receber a lista criada, por conta que foi passado somente uma variável.
        
        if len(partes) != 3: # Continuar a pedir o endereço se o comprimento da lista não for 3.
            print("""
                    Tente novamente. Lembrando que tem que ser no formato abaixo!                        
                        logradouro, nro - bairro - cidade/sigla estado
                """)
            continue
        else: 
            # Desempacota a lista em 3 partes e tira espaços a esquerda e direita
            rua_nro, bairro, cidade_sigla = [parte.strip() for parte in partes]
            
            # cria uma lista sendo dividida pela "," com o logradouro e número do endereço .
            logradouro_partes = rua_nro.split(",")
            
            # faz o desempacotamento da lista logradouro_partes tirando os espaços a esquerda e direita e colocando cada um em sua devida variável. 
            logradouro, numero = [log.strip() for log in logradouro_partes]
                
            # print(f"logradouro: {logradouro}, numero: {numero} - bairro: {bairro} - cidade/sigla: {cidade_sigla}")
            break
    "===================================================================================================================================="
    
    "================================================ Adiciona à lista um dicionário ===================================================="
    usuarios.append(
        {"Nome": name,
         "Nascimento": nascimento_formatado, 
         "CPF": cpf,
         "Endereço": 
         {"Logradouro": logradouro, "Número": numero,"Bairro": bairro, "Cidade_sigla": cidade_sigla}
         })
    print("✅ Usuário cadastrado com sucesso!")
    return usuarios
    "===================================================================================================================================="
       

def nova_conta(agencia, numero_conta, usuarios, contas): # Cadastro de conta para usuário
    cpf = input("Informe o CPF do usuário: ").strip()
    
    # Inicia a variável com valor padrão None
    usuario = None

    # Valida se cpf estiver dentro de user que recebeu os valores de usuarios.
    for user in usuarios:
        if cpf in user["CPF"]:
            usuario = user
            break

    # Faz a atribuição do dicionário, para depois adicionar à lista.
    if usuario:
        numero_conta = len(contas) + 1
        conta = {
            "Agência": agencia,
            "Nº Conta": numero_conta,
            "CPF": cpf
        }
        contas.append(conta)
        print("✅ Conta criada com sucesso!")
        return contas
    else:
        print("❌ Usuário não encontrado, cadastre o usuário primeiro!")
        return contas
        

def saque(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUE): # Estrutura base do saque
    
    excedeu_limite = valor > limite
    excedeu_saldo = valor > saldo
    excedeu_quantidade_saque = numero_saques >= LIMITE_SAQUE
    saques_disponiveis =  LIMITE_SAQUE - numero_saques

    # Verificação para ver se vai passar pelas verificações de saldo negativo, excedeu limite de saque e saque diário.
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print(f"Operação falhou! Limite de saque excedido você tem R$ {limite:.2f} por saque.")
    elif excedeu_quantidade_saque:
        print("Operação falhou! Limite diario de saque excedido.")
    
    # Caso passe vai verificar se o valor digitado e maior que zero.
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}💸\n"
        numero_saques += 1
        print(f"✅ Saque de R${valor:.2f} realizado com sucesso!💸")
    
    # Caso não seja maior que zero vai exibir a mensagem abaixo e retornar para o menu principal.
    else:
        print("❌ Valor inválido. Digite um valor maior que zero.")
    
    return saldo, extrato, numero_saques
    

def deposito(saldo, valor, extrato, /): # Estrutura base do depósito
    
    # Mesma verificação do saque para ver se o valor digitado é maior que zero.
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}💰\n"
        print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!😁")

    # Caso não seja maior que zero vai exibir a mensagem abaixo e retornar para o menu principal.
    else:
        print("❌ Valor inválido. Digite um valor maior que zero.")
    
    return saldo, extrato


def extrato_total(saldo, /, *, extrato): # Estrutura para exibir o Extrato Bancário
    print(f"\n{" EXTRATO BANCÁRIO ".center(40, "=")}\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}💰" if saldo > 0 else f"\nSaldo: R$ {saldo:.2f}😞")
    print("=" * 40)


def main():
    limite = 500
    saldo = 0
    extrato = ""
    numero_saques = 0
    
    agencia = AGENCIA
    numero_conta = 1
    usuarios = []
    contas = []

    while True:
        entry = input(menu)
        apagar_terminal()

        if entry == "d": # Verifica se a entrada do usuário foi "d" para pedir o valor do depósito.
            valor = float(input("Digite o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)
        
        elif entry == "s": # Verifica se a entrada do usuário foi "s" para pedir o valor do saque.
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato, numero_saques = saque(
                saldo=saldo, extrato=extrato,
                valor=valor, limite=500, 
                numero_saques=numero_saques, LIMITE_SAQUE=LIMITE_SAQUE
            )
        
        elif entry == "e": # Verifica se a entrada do usuário foi "e" para retornar o Extrato Bancário.
            extrato_total(saldo, extrato=extrato)
        
        elif entry == "nu": # Se a entrada do usuário foi "nu" vai para a criação de novo usuário.
            usuarios = novo_usuario(usuarios)
        
        elif entry == "nc": # Se a entrada do usuário foi "nc" vai para a criação de nova conta.
            contas = nova_conta(agencia, numero_conta, usuarios, contas)
        
        elif entry == "q": # Se a entrada do usuário foi "q" vai finalizar o programa.
            print("🕊️  Tenha um excelente dia! 🤝")
            break
        # Caso nenhuma das opções acima foi selecionada vai retornar a mensagem de erro e pedir novamente alguma opção que seja correta.
        else:
            print("❌ Opção inválida, por favor digite a opção correta.")


if __name__ == "__main__":
    main()    