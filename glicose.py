glicose: float

glicose = float(input("Digite a medida da glicose: "))

print("CLASSIFICACAO: ", end="")

if glicose <= 100:
    print("Normal")
elif glicose <= 140:
    print("Elevado")
else:
    print("Diabetes")
