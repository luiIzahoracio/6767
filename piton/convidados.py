convidados = []
for i in range (1,4):
    nome = input(f"digite o nome do convidado {i}:")
    convidados.append(nome)
print(f"sua lista de convidados tem {len(convidados)} pessoas: {convidados[0]}")