nome: str
valorH:float; pagamento: float
horasT: int

nome = input("Nome: ")
valorH = float(input("Valor por hora: "))
horasT = int(input("Horas trabalhadas: "))

pagamento = horasT * valorH

print(f"O pagamento para {nome} deve ser {pagamento:.2f}")
