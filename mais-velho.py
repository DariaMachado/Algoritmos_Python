n: int; i: int; maisVelho: int; posicao: int

n = int(input("Quantas pessoas voce vai digitar? "))

nome: [str] = [0 for x in range(n)]
idade: [int] = [0 for x in range(n)]

for i in range(0, n):
    print(f"Dados da {i + 1}a pessoa:")
    nome[i] = input("Nome: ")
    idade[i] = int(input("Idade: "))

maisVelho = idade[0]
posicao = 0

for i in range(0, n):
    if idade[i] > maisVelho:
        maisVelho = idade[i]
        posicao = i

print(f"PESSOA MAIS VELHA: {nome[posicao]}")
