valor = float(input("valor da compra: "))
cupom = input("tem cupom? (S/N):")

if valor > 200 or cupom == "S":
    print(f"parabens! Na compra de R$ {valor:.2f}, o frete é gratis.")
else:
    print(f"compra de R$ {valor:.2f} sem cupom: frete fixo de R$ 20")