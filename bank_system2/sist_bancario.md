# Nesse arquivo estarei explicando sobre o arquivo sistema_bancario_new_version.py.

### A proposta desse Desafio da [DIO](https://www.dio.me/) do Bootcamp (Santander 2025 - Back-End Python), era de melhorar o Sistema Bancário que já tinhamos feito antes, a proposta era de separar todo o código em funções e acrescentar mais duas sendo elas Cadastrar Usuário e Cadastrar Conta.


### **Entre o projeto adicionei também alguns emojis e respostas mais intuitivas de fácil compreensão para os usuários.**

###  1º **apagar_terminal()** 
Não precisava, mas quis colocar para não deixar o terminal cheio com as funções que o usuário já tinha escolhido e preenchido o que precisava, ou seja, foi para ficar melhor a visibilidade do usuário. Nesta função importei do módulo da biblioteca padrão do Python o [OS](https://docs.python.org/3/library/os.html#module-os) de dentro dela importei o [system](https://docs.python.org/3/library/os.html#os.system) e o [name](https://docs.python.org/3/library/os.html#os.name).
- *Função responsável por limpar a tela do terminal/console, tornando a interface do usuário mais limpa e organizada. Funciona tanto em sistemas Windows (cls) quanto em Unix/Linux/Mac (clear)*


### 2º **novo_usuario(usuarios)**
Realiza o cadastro de novos usuários.
- *Válida o nome para garantir que contém apenas letras.*
- *Valida a data de nascimento, aceitando os formatos dd/mm/aaaa ou dd-mm-aaaa, e verifica se o usuário tem pelo menos 18 anos.*
- *Valida o CPF, garantindo que tenha 11 dígitos numéricos e que não haja outro usuário cadastrado com o mesmo CPF.*
- *Solicita e valida o endereço no formato correto (logradouro, número - bairro - cidade/sigla).*
- *Ao final, adiciona o novo usuário à lista de usuários cadastrados.*

### 3º **nova_conta(agencia, numero_conta, usuarios, contas)** 
Cria uma nova conta para o usuário, além disso mais de que somente uma mais quantas ele quiser.
- *Solicita o CPF para identificar o usuário.*
- *Verifica se o usuário existe na lista de usuários.*
- *Se encontrado, cria uma nova conta para o usuário, associando o número da conta, agência e CPF.*
- *Adiciona a nova conta à lista de contas existentes.*

### 4º **saque(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUE)**
Função responsável por realizar o saque bancário.
- *Verifica se o valor do saque é válido (positivo).*
- *Confere se o saldo é suficiente para o saque.*
- *Verifica se o valor não ultrapassa o limite de saque por operação.*
- *Controla o número máximo de saques diários permitidos.*
- *Atualiza o saldo, extrato e número de saques realizados após um saque bem-sucedido.*
- *Mostra mensagens de erro ou sucesso para o usuário.*

### 5º **deposito(saldo, valor, extrato, /)**
Função responsável por realizar depósitos na conta bancária.
- *Verifica se o valor do depósito é positivo.*
- *Atualiza o saldo e o extrato com o valor depositado.*
- *Mostra mensagens de sucesso ou erro conforme o caso.*

### 6º **extrato_total(saldo, /, \*,extrato)**
Função para exibir o extrato bancário completo.
- *Limpa o terminal antes de exibir o extrato.*
- *Mostra todas as transações realizadas (saques e depósitos).*
- *Exibe o saldo atual formatado, com um emoji diferente para saldo positivo ou negativo.*

### 7º **main()**
Função principal, responsável por executar o loop do programa.
- *Inicializa variáveis e listas (saldo, limite, usuários, contas, etc).*
- *Exibe o menu principal e solicita a ação do usuário.*
- *Chama as funções correspondentes de acordo com a escolha do usuário (depósito, saque, novo usuário, nova conta, extrato, sair).*
- *Controla o fluxo principal do sistema bancário.*
