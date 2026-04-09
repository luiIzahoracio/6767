a, b, c = int(input("lado A")), int(input("lado B")), int(input("lado C"))
if a < b + c and b > a + c and c < a + b:
    print(f"as medidas {a}, {b}, {c} foram um triangulo válido.")
else:
     print(f"as medidas {a}, {b}, {c} nao podem formar um triangulo.")