edades = [20, 35, 23, 65, 56]

def promedio_edades(edades):
    suma = 0
    for n in edades:
        suma = suma + n
    return suma / len(edades)

promedio = promedio_edades(edades)
print(f"El promedio de las edades es {promedio}")