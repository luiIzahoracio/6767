print (" === Simulador de Intercambio: Londres ===")
orcamento_reais = float(input("quanto você tem guardado em reais? R$:"))
cotacao_libra = float(input("qual é a cotação atual de libras? "))

saldo_libra = orcamento_reais/cotacao_libra
print(f"seu saldo convertido é de {saldo_libra:2f}")

custo_curso = float(input("valor do curso de inglês em libras"))
custo_moradia = float("custo mensal da moradia:")
meses = int(input("quantos meses você pretender ficar?"))

custo_total_libras = custo_curso + (custo_moradia * meses)

if saldo_libra >= custo_total_libras:
    sobra = saldo_libra - custo_total_libras
    print(f"/n financeiro: APROVADO! O custo total é: {custo_total_libras}")
    print(f"ainda sobrará {sobra} para passeios.")

else:
    falta_libras = custo_total_libras - saldo_libra
    falta_reais = falta_libras * cotacao_libra
    print(f"/n Financeiro: REPROVADO. Faltam: {falta_libras:.2f}(aprox. R$ {falta_reais})")
     
print("/n ----verificaçao de documentação e perfil ----")
idade = int(input("qual a sua idade ?"))
ingles_fluente = input("possui certificado de fluência? (s/n):")
passaporte_europeu = input ("possui passaporte europeu ?(s/n):")

if idade >= 16 and ingles_fluente == "s":
    print("Você pode aplicar o visto de 'estudo de trabalho'")
else:
    print("Você pode apenas estudar; o visto de trabalho não será permitido")

if passaporte_europeu == "s" or (idade < 18 and ingles_fluente == "s"):
    print("Resultado: você tem direito ao 'apoio jovem talento' ou inserção de visto!")

print ("==== Boa viagem ====")