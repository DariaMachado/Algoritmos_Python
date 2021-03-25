n: int; i: int
somaV: float; mediaV: float

n = int(input("Quantos elementos vai ter o vetor? "))

vet: [float] = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = float(input("Digite um numero: "))

print()
somaV = 0

for i in range(0, n):
    somaV = somaV + vet[i]

mediaV = somaV / n
print(f"MEDIA DO VETOR = {mediaV:.3f}")

print("ELEMENTOS ABAIXO DA MEDIA:")

for i in range(0, n):
    if vet[i] < mediaV:
        print(vet[i])
