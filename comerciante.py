n: int; i: int; abaixo: int; entre: int; acima: int
totalC: float; totalV: float; lucroT: float

n = int(input("Serao digitados dados de quantos produtos? "))

produto: [str] = [0 for x in range(n)]
compra: [float] = [0 for x in range(n)]
venda: [float] = [0 for x in range(n)]
perlucro: [float] = [0 for x in range(n)]


for i in range(0, n):
    print(f"Produto {i + 1}:")
    produto[i] = input("Nome: ")
    compra[i] = float(input("Preco de compra: "))
    venda[i] = float(input("Preco de venda: "))

for i in range(0, n):
    perlucro[i] = (venda[i] - compra[i]) / compra[i] * 100

abaixo = 0
entre = 0
acima = 0

for i in range(0, n):
    if perlucro[i] < 10.0:
        abaixo = abaixo + 1
    elif perlucro[i] <= 20.0:
        entre = entre + 1
    else:
        acima = acima + 1

totalC = 0
totalV = 0

for i in range(0, n):
    totalC = totalC + compra[i]
    totalV = totalV + venda[i]

lucroT = totalV - totalC

print("\nRELATORIO:")
print(f"Lucro abaixo de 10%: {abaixo}")
print(f"Lucro entre 10% e 20%: {entre}")
print(f"Lucro acima de 20%: {acima}")
print(f"Valor total de compra: {totalC:.2f}")
print(f"Valor total de venda: {totalV:.2f}")
print(f"Lucro total: {lucroT:.2f}")

