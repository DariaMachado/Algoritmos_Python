valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))
valor3 = int(input("Terceiro valor: "))

if valor1 < valor2 and valor1 < valor3:
    menor = valor1
elif valor2 < valor3:
    menor = valor2
else:
    menor = valor3

print(f"MENOR = {menor}")
