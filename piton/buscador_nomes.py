nomes = ["Wiliian", "Dudu", "Gui", "Gigi"]
busca = input("quem você deseja buscar?").capitalize()

if busca in nomes:
    print (f"sijm, {busca} está na lista!")
else:
    print (f"o nome {busca} nao foi encontrado.")