import textwrap

# Listas globais para armazenar usuários e contas
usuarios = []
contas = []

AGENCIA = "0001"


# Função para criar um novo usuário
def criar_usuario(nome, data_nascimento, cpf, endereco):
    cpf = "".join(filter(str.isdigit, cpf))  # Remove caracteres não numéricos do CPF
    if any(usuario["cpf"] == cpf for usuario in usuarios):
        print("Erro: Já existe um usuário cadastrado com esse CPF.")
        return

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")


# Função para filtrar um usuário pelo CPF
def buscar_usuario(cpf):
    cpf = "".join(filter(str.isdigit, cpf))  # Remove caracteres não numéricos do CPF
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


# Função para criar uma nova conta bancária
def criar_conta(cpf):
    usuario = buscar_usuario(cpf)
    if not usuario:
        print("Erro: Usuário não encontrado. Verifique o CPF informado.")
        return

    numero_conta = len(contas) + 1
    conta = {
        "agencia": AGENCIA,
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0.0,
        "extrato": [],
        "numero_saques": 0,
    }
    contas.append(conta)
    print(f"Conta criada com sucesso! Agência: {AGENCIA}, Conta: {numero_conta}")


# Função para listar todas as contas bancárias
def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    for conta in contas:
        print("=" * 40)
        print(f"Agência: {conta['agencia']}")
        print(f"Número da Conta: {conta['numero_conta']}")
        print(f"Titular: {conta['usuario']['nome']}")
    print("=" * 40)


# Função para realizar depósito (apenas por posição)
def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("Erro: O valor do depósito deve ser positivo.")
        return saldo, extrato

    saldo += valor
    extrato.append(f"Depósito: R$ {valor:.2f}")
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato


# Função para realizar saque (apenas por nome)
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("Erro: Limite de saques diários atingido.")
        return saldo, extrato

    if valor > limite:
        print("Erro: O valor do saque excede o limite permitido de R$ 500,00.")
        return saldo, extrato

    if valor > saldo:
        print("Erro: Saldo insuficiente.")
        return saldo, extrato

    saldo -= valor
    extrato.append(f"Saque: R$ {valor:.2f}")
    numero_saques += 1
    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    
    return saldo, extrato


# Função para exibir o extrato (posição e nome)
def exibir_extrato(saldo, /, *, extrato):
    print("\nExtrato da Conta")
    print("-" * 40)
    
    if not extrato:
        print("Não foram realizadas movimentações.")
    
    for transacao in extrato:
        print(transacao)
        
    print("-" * 40)
    print(f"Saldo Atual: R$ {saldo:.2f}")
    print("-" * 40)


# Menu principal do sistema bancário
def menu():
    while True:
        opcao = input(textwrap.dedent("""
            \n========== Sistema Bancário ==========
            [1] Cadastrar Usuário
            [2] Criar Conta Bancária
            [3] Listar Contas Bancárias
            [4] Depositar
            [5] Sacar
            [6] Exibir Extrato
            [7] Sair
            Escolha uma opção: """))

        if opcao == "1":
            nome = input("Nome completo: ")
            data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
            cpf = input("CPF (somente números): ")
            endereco = input(
                "Endereço (logradouro, número - bairro - cidade/UF): "
            )
            criar_usuario(nome, data_nascimento, cpf, endereco)

        elif opcao == "2":
            cpf = input("Informe o CPF do usuário: ")
            criar_conta(cpf)

        elif opcao == "3":
            listar_contas()

        elif opcao == "4":
            cpf = input("Informe o CPF do titular da conta: ")
            conta = next((c for c in contas if c["usuario"]["cpf"] == cpf), None)
            if not conta:
                print("Erro: Conta não encontrada.")
                continue

            valor = float(input("Informe o valor do depósito: "))
            conta["saldo"], conta["extrato"] = depositar(
                conta["saldo"], valor, conta["extrato"]
            )

        elif opcao == "5":
            cpf = input("Informe o CPF do titular da conta: ")
            conta = next((c for c in contas if c["usuario"]["cpf"] == cpf), None)
            if not conta:
                print("Erro: Conta não encontrada.")
                continue

            valor = float(input("Informe o valor do saque: "))
            
            # Chama a função de saque e atualiza o saldo e o extrato da conta.
            conta["saldo"], conta["extrato"] = sacar(
                saldo=conta["saldo"],
                valor=valor,
                extrato=conta["extrato"],
                limite=500,
                numero_saques=conta["numero_saques"],
                limite_saques=3,
            )
            
            # Incrementa o contador de saques apenas se o saque foi bem-sucedido.
            if valor <= 500 and valor <= conta["saldo"]:
                conta["numero_saques"] += 1

        elif opcao == "6":
            cpf = input("Informe o CPF do titular da conta: ")
            conta = next((c for c in contas if c["usuario"]["cpf"] == cpf), None)
            if not conta:
                print("Erro: Conta não encontrada.")
                continue

            exibir_extrato(conta["saldo"], extrato=conta["extrato"])

        elif opcao == "7":
            print("Saindo do sistema... Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
