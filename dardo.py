distancia1: float; distancia2: float; distancia3: float; maiorD: float

print("Digite as tres distancias: ")
distancia1 = float(input())
distancia2 = float(input())
distancia3 = float(input())

if distancia1 > distancia2 and distancia1 > distancia3:
    maiorD = distancia1
elif distancia2 > distancia3:
    maiorD = distancia2
else:
    maiorD = distancia3

print(f"MAIOR DISTANCIA = {maiorD:.2f}")

