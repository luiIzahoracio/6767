idade = int(input("idade:"))
if idade >= 5 and idade <= 10:
    categoria = "infantil"
elif idade >= 11 and idade <=17:
    categoria = "juvenil"
elif idade >=18:
    categoria = "adulto"
else:
    categoria = "nao permitida"
print(f"atleta com {idade} anos está na categoria: {categoria}.")