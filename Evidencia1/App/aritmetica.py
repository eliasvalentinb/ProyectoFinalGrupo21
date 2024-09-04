
# 1. sumar(): Suma de dos número reales (float), recibe dos números y devuelve la suma de los mismos
def sumar(a: float, b: float) -> float:
    try:
        resultado = round(a + b, 2)
        return resultado
    except TypeError:
        print("Valores no permitidos.")

# 2. restar(): Resta de dos número reales (float), recibe dos números 
# y devuelve la resta del primer número menos el segundo
def restar(a: float, b: float) -> float:
    try:
        resultado = round(a - b, 2)
        return resultado
    except TypeError:
        print("Valores no permitidos.")

# 3. dividir(): División de dos números reales (float), recibe dos números  y devuelve el resultado de dividir el primer número por el segundo.
# Nota: Aquí considerar en la división el caso de división por cero y hacer un manejo de excepción.
def dividir(a: float, b: float) -> float:
    try:
        result = round(a / b, 2)
        if b == 0:
            raise ValueError("No se puede dividir por 0")
        return result
    except TypeError:
        print("Valores no permitidos.")

# 4. multiplicar(): Multiplicación de dos números reales (float), recibe dos números y devuelve el resultado de multiplicarlos entre sí.
def multiplicar(a: float, b: float) -> float:
    try:
        resultado = round(a * b, 2)
        return resultado
    except TypeError:
        print("Valores no permitidos.")

# 5. sumar_n(): Suma de n número reales (float), recibe una cantidad variable de números y devuelve la suma de los mismos
def sumar_n(*numeros: float) -> float:
    try:
        resultado = round(sum(numeros), 2)
        return resultado
    except TypeError:
        print("Valores no permitidos.")
        return 0.0

#  6. promedio_n: Promedio de n número reales (float), recibe una cantidad variable de números y devuelve el valor promedio de los mismos
def promedio_n(*numeros: float) -> float:
    if not numeros:
        raise ValueError("Se debe ingresar al menos un número.")
    return round(sum(numeros) / len(numeros), 2)
