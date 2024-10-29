# Sistema de Gerenciamento de Estacionamento

Este projeto implementa um sistema simples para gerenciar carros em um estacionamento. Utilizando uma lista, o sistema permite adicionar, remover e listar carros, proporcionando uma forma prática de controle.

## Funcionalidades

### 1. Adicionar Carro
Permite ao usuário adicionar um carro ao estacionamento, registrando a marca, cor e placa.

**Exemplo:**
```python
adicionar_carro("Fusca", "azul", "ABC-1234")
```

### 2. Remover Carro
Remove um carro do estacionamento com base na placa informada.

**Exemplo:**
```python
remover_carro("ABC-1234")
```

### 3. Listar Carros
Exibe todos os carros atualmente no estacionamento, com detalhes sobre marca, cor e placa.

**Exemplo:**
```python
listar_carros()
```

### 4. Interface de Usuário
O sistema inclui uma interface de linha de comando que permite ao usuário interagir com as funcionalidades de gerenciamento.

## Estrutura do Código

- **Lista `estacionamento`:** Armazena os carros no estacionamento.
- **Funções:**
  - `adicionar_carro(marca, cor, placa)`: Adiciona um carro.
  - `remover_carro(placa)`: Remove um carro pela placa.
  - `listar_carros()`: Lista todos os carros no estacionamento.
- **Loop de interação:** Permite que o usuário escolha ações até decidir sair.

