peso = input("Digite su peso en Kg")
estatura = input ("Digite su estatura en metros")
imc = round (float(peso)/float(estatura)**2,2)
print ("Tu índice de masa corporal es: ", str(imc))