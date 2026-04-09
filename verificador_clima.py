temp = float(input("temperatura:"))
if temp <10 or temp >35:
    print(f"atenção: {temp}°C é considerado clima extremo!")
else:
    print(f"a tempetura de {temp}°C está agradável.")