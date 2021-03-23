inicial: int; final: int; duracao: int

inicial = int(input("Hora inicial: "))
final = int(input("Hora final: "))

if inicial >= final:
    duracao = 24 - inicial + final
else:
    duracao = final - inicial

print(f"O JOGO DUROU {duracao} HORA(S)")