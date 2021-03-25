n: int; i: int; somaPares: int; contPares: int
mediaPares: float

n = int(input("Quantos elementos vai ter o vetor? "))

vet: [int] = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = int(input("Digite um numero: "))

somaPares = 0
contPares = 0

for i in range(0, n):
    if vet[i] % 2 == 0:
        somaPares = somaPares + vet[i]
        contPares = contPares + 1

if contPares == 0:
    print("NENHUM NUMERO PAR")
else:
    mediaPares = somaPares / contPares
    print(f"MEDIA DOS PARES = {mediaPares:.1f}")
