m: int; n: int; j: int; i: int

m = int(input("Quantas linhas vai ter cada matriz? "))
n = int(input("Quantas colunas vai ter cada matriz? "))

A: [[int]] = [[0 for x in range(n)] for x in range(m)]
B: [[int]] = [[0 for x in range(n)] for x in range(m)]
C: [[int]] = [[0 for x in range(n)] for x in range(m)]

print("Digite os valores da matriz A:")

for i in range(0, m):
    for j in range(0, n):
        A[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("Digite os valores da matriz B:")

for i in range(0, m):
    for j in range(0, n):
        B[i][j] = int(input(f"Elemento [{i},{j}]: "))

for i in range(0, m):
    for j in range(0, n):
        C[i][j] = A[i][j] + B[i][j]

print("MATRIZ SOMA:")

for i in range(0, m):
    for j in range(0, n):
        print(f"{C[i][j]} ", end="")
    print()




