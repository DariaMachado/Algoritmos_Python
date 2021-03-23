distancia: int
combustivel: float; consumoM: float

distancia = int(input("Distancia percorrida: "))
combustivel = float(input("Combustível gasto: "))

consumoM = distancia / combustivel

print(f"Consumo medio = {consumoM:.3f}")
