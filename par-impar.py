numero: int; n: int; i: int

n = int(input("Quantos numeros voce vai digitar? "))

for i in range(0, n):
    numero = int(input("Digite um numero: "))

    if numero == 0:
        print("NULO")
    else:
        if numero % 2 == 0:
            print("PAR ", end="")
        else:
            print("IMPAR ", end="")

        if numero > 0:
            print("POSITIVO")
        else:
            print("NEGATIVO")
