opcao = " "
while opcao != "3":
    print ("\n[1] saudar")
    print ("\n[2] calcular dobro")
    print ("[3] sair")
    opcao = input("escolha uma opçao: ")
    if opcao =="1":
        print ("ola! tenha um otimo dia de aula. ")
    elif opcao =="2":
        n = float(input("digite o número: "))
        print (f"o dobro de {n} é {n*2}")
    elif opcao =="3":
        print ("saindo do sistema...")
    else:
        print ("opção inválida")