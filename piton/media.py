notas = []
for i in range (1,5):
    n = float(input("digite sua nota"))
    notas.append(n)

media = sum(notas)/len (notas)
print(f"notas registradas: {notas}")
print(f"a média da turma é: {media:.1f}")