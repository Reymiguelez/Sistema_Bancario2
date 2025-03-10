# Sistema_Bancario2
Sistema bancário em python com opção de depósito, saque, extrato, cadastro de usuário (cliente do banco, cadastrar conta bancaria (vincular com o usuario) e listar contas. 

Funcões de Saque, deposito e extrato em funcoes separadas. 

- O sistema permiti apenas 3 saques diários com o limite máximo de R$500,00 por saque. Se o usuário introduzir algum valor acima de R$500,00, deverá ser apresentado para o usuário uma mensagem que excede o limite diário, e não deverá ser contabilizado como saque.

- A opção de visualizar o extrato lista todos os depósitos e saques realizados na conta utilizando o formato R$ xxx.xx Exemplo: 1500.45 = R$ 1500.45.

- O depósito não pode ter valor negativo, apenas positivo.

- A função de saque recebe os argumentos apenas por nome (keyword only). Argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Retorno: saldo e extrato.

- A funcão depósito recebe os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

- A funcão extrato recebe os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.

- O programa armazena os usuários em lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é ua string com o formato: logradouro, número, bairro, cidade / sigla estado. Deve ser armazenado somente os números do CPF.  Não se pode cadastrar 2 usuários ou mais com o mesmo CPF.

- O programa armazena contas em uma lista, uma conta é composta por: agencia, numero da conta e usuario. O numero da contaé sequencial, inciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário.

- O usuário é vinculado a uma conta, filtrando a lista de usuarios buscando o número do CPF informado para cada usuario da lista.
