n: int; i: int

n = int(input("Quantos alunos serao digitados? "))

nome: [str] = [0 for x in range(n)]
nota1: [float] = [0 for x in range(n)]
nota2: [float] = [0 for x in range(n)]


for i in range(0, n):
    print(f"Digite nome, primeira e segunda nota do {i + 1}o aluno:")
    nome[i] = input()
    nota1[i] = float(input())
    nota2[i] = float(input())

print("Alunos aprovados:")

for i in range(0, n):
    media = (nota1[i] + nota2[i]) / 2

    if media[i] >= 6.0:
        print(nome[i])
