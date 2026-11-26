import math

# Pitagoras

def pitagoras(a: int, b: int) -> float:
    c = math.sqrt(a**2 + b**2)
    return c

# Circle

def area_circulo(radio: float) -> float:
    a = math.pi * radio**2
    return a

# Volumen

def volumen_cilindro(radio: float, altura: float) -> float:
    v = math.pi * radio**2 * altura
    return v

# Celcius to Fahrenheit

def celcius_to_fahrenheit(celcius: float) -> float:
    f = (celcius*9/5)+32
    return f

# IMC

def calcular_imc(peso:float, altura:float) -> str:
    imc = peso / (altura**2)

    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc >= 30:
        return "Obesidad"
    else:
        return "Indefinido, vuelve a intentar"

# cuadratica

def resolver_cuadratica(a, b, c):
    d = (b**2) - 4 * a * c

    if d < 0:
        return "No hay soluciones reales"
    elif d == 0:
        solucion = -b / (a*2)
        return solucion
    else:
        x1 = (-b +math.sqrt(d)) / (a*2)
        x2 = (-b -math.sqrt(d)) / (a*2)
        return x1, x2

# Factorial

def calcular_factorial(n: int) -> int:
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i

    return resultado 

print(calcular_factorial(2))