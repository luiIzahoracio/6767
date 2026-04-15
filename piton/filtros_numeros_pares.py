limite = int(input("até qual número quer ver os pares ? "))
for n in range (1, limite + 1 ):
    if n %2 == 0:
        print(f"o numeroi {n} é par ")