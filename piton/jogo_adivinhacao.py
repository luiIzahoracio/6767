segredo = 7
tentativas = 3 

print("adivinhe o numero secreto (1 a 10. Você tem tres chances!)")

while tentativas > 0:
    chute = int(input(f"tentativas restantes ({tentativas}):"))

    if chute == segredo:
        print(f"´parabens o número era {segredo}.")
        tentativas=0
    else:
        tentativas = tentativas -1
        if tentativas >0:
            print("errou tente denovo.")
        else:
            print(f"suas chances acabaram. O número era {segredo}")