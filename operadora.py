minutos: int
valor: float

minutos = int(input("Digite a quantidade de minutos: "))

valor = 50.00

if minutos > 100:
    valor = valor + (minutos - 100) * 2

print(f"Valor a pagar: R$ {valor:.2f}")
