# Lista para armazenar os carros no estacionamento
estacionamento = []
 
# Função para adicionar um carro ao estacionamento
def adicionar_carro(marca, cor, placa):
    carro = {
        "marca": marca,
        "cor": cor,
        "placa": placa
    }
    estacionamento.append(carro)
    print(f"Carro com placa {placa} adicionado ao estacionamento.")
 
# Função para remover um carro do estacionamento com base na placa
def remover_carro(placa):
    for carro in estacionamento:
        if carro["placa"] == placa:
            estacionamento.remove(carro)
            print(f"Carro com placa {placa} removido do estacionamento.")
            return
    print(f"Carro com placa {placa} não encontrado.")
 
# Função para listar todos os carros no estacionamento
def listar_carros():
    if estacionamento:
        print("Carros no estacionamento:")
        for carro in estacionamento:
            print(f"- Marca: {carro['marca']}, Cor: {carro['cor']}, Placa: {carro['placa']}")
    else:
        print("O estacionamento está vazio.")
 
# Estrutura de repetição para simulação do sistema
while True:
    print("\nSistema de Gerenciamento de Estacionamento")
    print("1. Adicionar Carro")
    print("2. Remover Carro")
    print("3. Listar Carros")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        marca = input("Digite a marca do carro: ")
        cor = input("Digite a cor do carro: ")
        placa = input("Digite a placa do carro: ")
        adicionar_carro(marca, cor, placa)
        
    elif opcao == "2":
        placa = input("Digite a placa do carro a ser removido: ")
        remover_carro(placa)
        
    elif opcao == "3":
        listar_carros()
        
    elif opcao == "4":
        print("Saindo do sistema...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")