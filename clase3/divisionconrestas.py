def division_con_resta(dividendo, divisor):
    if dividendo < divisor:
        return 0, dividendo
    cociente, residuo = division_con_resta(dividendo - divisor, divisor)
    return cociente + 1, residuo

num1 = 20
num2 = 4
resultado, residuo = division_con_resta(num1, num2)
print(f"{num1} / {num2} = Cociente: {resultado}, Residuo: {residuo}")
