def multiplicacion_con_suma(a, b):
    if b == 0:
        return 0
    return a + multiplicacion_con_suma(a, b - 1)

num1 = 4
num2 = 5
resultado = multiplicacion_con_suma(num1, num2)
print(f"{num1} * {num2} = {resultado}")

    
    
    