n: int; i: int; contPares: int

n = int(input("Quantos numeros voce vai digitar? "))

vet: [int] = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = int(input("Digite um numero: "))

print("\nNUMEROS PARES:")

contPares = 0

for i in range(0, n):
    if vet[i] % 2 == 0:
        print(f"{vet[i]} ", end="")
        contPares = contPares + 1


print(f"\n\nQUANTIDADE DE PARES = {contPares}")
