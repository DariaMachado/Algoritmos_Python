n: int; i: int; contM: int; contF: int
menorAlt: float; maiorAlt: float; somaAlt: float; mediaAlt: float

n = int(input("Quantas pessoas serao digitadas? "))

altura: [float] = [0 for x in range(n)]
genero: [str] = [0 for x in range(n)]

for i in range(0, n):
    altura[i] = float(input(f"Altura da {i + 1}a pessoa:"))
    genero[i] = input(f"Genero da {i + 1}a pessoa:")

menorAlt = altura[0]
maiorAlt = altura[0]

for i in range(0, n):
    if altura[i] < menorAlt:
        menorAlt = altura[i]

    if altura[i] > maiorAlt:
        maiorAlt = altura[i]

print(f"Menor altura = {menorAlt:.2f}")
print(f"Maior altura = {maiorAlt:.2f}")

somaAlt = 0
contF = 0
contM = 0

for i in range(0, n):
    if genero[i] == 'F':
        somaAlt = somaAlt + altura[i]
        contF = contF + 1
    else:
        contM = contM + 1

mediaAlt = somaAlt / contF

print(f"Media das alturas das mulheres = {mediaAlt:.2f}")
print(f"Numero de homens = {contM}")
