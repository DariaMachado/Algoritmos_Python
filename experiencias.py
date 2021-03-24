n: int; i: int; coelhos: int; ratos: int; sapos: int; qtd: int; total: int
tipo: str
perC: float; perR: float; perS: float

n = int(input("Quantos casos de teste serao digitados? "))

coelhos = 0
ratos = 0
sapos = 0

for i in range(0, n):
    qtd = int(input("Quantidade de cobaias: "))
    tipo = input("Tipo de cobaia: ")

    if tipo == 'C':
        coelhos = coelhos + qtd
    elif tipo == 'R':
        ratos = ratos + qtd
    elif tipo == 'S':
        sapos = sapos + qtd

total = coelhos + ratos + sapos
perC = coelhos / total * 100
perR = ratos / total * 100
perS = sapos / total * 100

print()
print("RELATORIO FINAL:")
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {perC:.2f}")
print(f"Percentual de ratos: {perR:.2f}")
print(f"Percentual de sapos: {perS:.2f}")
