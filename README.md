# 🏦Desafio do Sistema Bancário com Python🐍 

## Resolução do Desafio Sistema bancário.

### Este desafio consistia em ter quatro opções para o usuário escolher que é Depósito, Saque, Extrato e Sair.

- **Depósito** *Consiste em verificar se o valor depositado não é um valor negativo, exibindo o valor depositado com símbolo da moeda que é R$ e também formatado para mostrar 2 casas decimais depois do ponto flutuante. Também temos o adicionamento do valor que o usuário digitou de depósito na variável **saldo** e depois a inclusão a variável **extrato** para que assim quando for solicitado o extrato apareça quais operações foram feitas.*
- **Saque** *Na questão do saque temos a mesma verificação para ver se o usuário não colocou nenhum valor negativo, só que no saque temos um valor limite de cada saque que é de R$ 500,00 e 3 tentativas de saque por dia. Na opção de saque foi feita a subtração do valor sacado ao valor que continha na variável **saldo**.*
- **Extrato** *Caso fosse solicitado o extrato sem ao menos ter feito uma operação iria aparecer uma mensagem programada daquele bloco, mas caso tivesse tido algum deposito ou saque iria pegar o valor da variável **extrato** *Na parte do extrato foi usuado o if ternário para mostrar as respectivas mensagens caso não tivesse tido movimentação nenhuma e caso tivesse tido algum saque ou depósito iria aparecer a mensagem que tinha como depósito ou saque ou as mensagens, usei também o que foi aprendido no módulo sobre manipulação de strings.*
- **Sair** *Na opção sair apenas coloquei uma mensagem para não só simplesmente sair sem exibir nada.*