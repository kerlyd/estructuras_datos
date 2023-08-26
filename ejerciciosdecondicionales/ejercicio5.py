edad = int(input("¿Cuál es tu edad? "))
income = float(input("¿Cuales son tus ingresos mensuales?"))
if edad > 16 and income >= 1000:
    print("Tienes que cotizar")
else:
    print("No tienes que cotizar")