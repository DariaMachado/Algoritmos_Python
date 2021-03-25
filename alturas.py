n: int; i: int; nMenores: int
somaAlt: float; mediaAlt: float; perMenores: float

n = int(input("Quantas pessoas serao digitadas? "))

nome: [str] = [0 for x in range(n)]
idade: [int] = [0 for x in range(n)]
altura: [float] = [0 for x in range(n)]

for i in range(0, n):
    print(f"Dados da {i + 1}a pessoa:")
    nome[i] = input("Nome: ")
    idade[i] = int(input("Idade: "))
    altura[i] = float(input("Altura: "))

somaAlt = 0
print()

for i in range(0, n):
    somaAlt = somaAlt + altura[i]

mediaAlt = somaAlt / n
print(f"Altura média: {mediaAlt:.2f}")

nMenores = 0

for i in range(0, n):
    if idade[i] < 16:
        nMenores = nMenores + 1

perMenores = nMenores / n * 100
print(f"Pessoas com menos de 16 anos: {perMenores:.1f} %")

for i in range(0, n):
    if idade[i] < 16:
        print(nome[i])
