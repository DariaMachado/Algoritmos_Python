salario: float; novoSalario: float; aumento: float
porcentagem: int

salario = float(input("Digite o salario da pessoa: "))

if salario <= 1000:
    porcentagem = 20
elif salario <= 3000:
    porcentagem = 15
elif salario <= 8000:
    porcentagem = 10
else:
    porcentagem = 5

aumento = salario * porcentagem / 100
novoSalario = salario + aumento

print(f"Novo salario = R$ {novoSalario:.2f}")
print(f"Aumento = R$ {aumento:.2f}")
print(f"Porcentagem = {porcentagem} %")
