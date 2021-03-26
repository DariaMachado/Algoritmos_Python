n: int; i: int; j: int; linha: int; coluna: int
somaP: float

n = int(input("Qual a ordem da matriz? "))

mat: [[float]] = [[0 for x in range(n)] for x in range(n)]

for i in range(0, n):
    for j in range(0, n):
        mat[i][j] = float(input(f"Elemento [{i},{j}]: "))

somaP = 0

for i in range(0, n):
    for j in range(0, n):
        if mat[i][j] > 0:
            somaP = somaP + mat[i][j]

print(f"\nSOMA DOS POSITIVOS: {somaP:.1f}")

linha = int(input("\nEscolha uma linha: "))
print("LINHA ESCOLHIDA: ", end="")

for j in range(0, n):
    print(f"{mat[linha][j]:.1f} ", end="")

coluna = int(input("\n\nEscolha uma coluna: "))
print("COLUNA ESCOLHIDA: ", end="")

for i in range(0, n):
    print(f"{mat[i][coluna]:.1f} ", end="")

print("\n\nDIAGONAL PRINCIPAL:", end="")

for i in range(0, n):
    print(f"{mat[i][i]:.1f} ", end="")

for i in range(0, n):
    for j in range(0, n):
        if mat[i][j] < 0:
            mat[i][j] = mat[i][j] ** 2

print("\n\nMATRIZ ALTERADA:")

for i in range(0, n):
    for j in range(0, n):
        print(f"{mat[i][j]:.1f} ", end="")
    print()


