nota = float(input("digite a nota do aluno (0 a 10)"))
renda = float(input("digite a renda:"))
e_atleta = input("o aluno é atleta federado? (s/n):")

if nota >= 9.0 and (renda <= 2000 or e_atleta == "s"):
    print(f"resultado: bolsa de estudo aprovada para nota {nota}!")