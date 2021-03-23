a: float; b: float; c: float
areaQ: float; areaTri: float; areaTra: float

a = float(input("Digite a medida A: "))
b = float(input("Digite a medida B: "))
c = float(input("Digite a medida C: "))

areaQ = a ** 2
areaTri = (a * b)/ 2
areaTra = ((a + b) * c) / 2

print(f"AREA DO QUADRADO = {areaQ:.4f}")
print(f"AREA DO TRIANGULO = {areaTri:.4f}")
print(f"AREA DO TRAPEZIO = {areaTra:.4f}")
