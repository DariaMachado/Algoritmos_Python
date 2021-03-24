n: int; i: int; multiplicacao: int

n = int(input("Deseja a tabuada para qual valor? "))

for i in range(1, 11):
    multiplicacao = n * i
    print(f"{n} x {i} = {multiplicacao}")
