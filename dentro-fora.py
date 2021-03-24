n: int; i: int; fora: int; dentro: int; x: int

n = int(input("Quantos numeros voce vai digitar? "))

fora = 0
dentro = 0

for i in range(0, n):
    x = int(input("Digite um numero: "))

    if x < 10 or x > 20:
        fora = fora + 1
    else:
        dentro = dentro + 1

print(f"{dentro} DENTRO")
print(f"{fora} FORA")
