idades: float; media: float
cont: int; soma: int

print("Digite as idades: ")
idades = int(input())

if idades < 0:
    print("IMPOSSIVEL CALCULAR")
else:
    soma = 0
    cont = 0

    while idades >= 0:
       soma = soma + idades
       cont = cont + 1
       idades = int(input())

    media = soma / cont
    print(f"MEDIA = {media:.2f}")
