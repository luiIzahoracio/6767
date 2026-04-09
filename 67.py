renda = float(input("renda"))
meses = int(input("meses de trabalho:"))

if renda >= 2500 and meses >=12:
    print(f"emprestimo aprovado para renda de R$ {renda:.2f}")
else: 
    print(f"emprestimo negado. Requisito minimos não atingigdo.")
    