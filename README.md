# Custom Stack

Projeto em Python para estudo de testes automatizados sobre uma estrutura de pilha customizada (`CustomStack`) e uma regra de negócio para ordenar números sorteados da Mega Sena.

## O que foi implementado

- Correção da validação de pilha cheia na classe `CustomStack`.
- Ampliação da suíte de testes de unidade da `CustomStack`, cobrindo fluxos válidos e exceções.
- Implementação da classe `NumberAscOrder`, responsável por receber uma `CustomStack` e retornar uma lista ordenada em ordem crescente.
- Criação dos testes da `NumberAscOrder` para os cenários de pilha com 6 números e pilha vazia.

## Como preparar o ambiente

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Como testar

Para executar todos os testes:

```powershell
.\.venv\Scripts\python.exe -m pytest
```

Para executar os testes com relatório de cobertura:

```powershell
.\.venv\Scripts\python.exe -m pytest --cov=src --cov-report=term-missing
```
