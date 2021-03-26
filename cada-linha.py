n: int; i: int; j: int; maior:int

n = int(input("Qual a ordem da matriz? "))

mat: [[int]] = [[0 for x in range(n)] for x in range(n)]
maiorL: [int] = [0 for x in range(n)]

for i in range(0, n):
    for j in range(0, n):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))


for i in range(0, n):
    maior = mat[i][0]
    for j in range(0, n):
        if mat[i][j] > maior:
            maior = mat[i][j]

    maiorL[i] = maior

print("MAIOR ELEMENTO DE CADA LINHA:")

for i in range(0, n):
    print(maiorL[i])


