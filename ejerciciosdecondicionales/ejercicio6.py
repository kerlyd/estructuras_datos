name = input("¿Como es tu nombre?")
genero = input("¿Cual es tu genero M o H? ")

if genero == "M" :
    if name.lower() > "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() < "n":
        group = "A"

    else:
        group = "B"
    
    print("Tu grupo es " + group)


        