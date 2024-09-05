import time
import random
from datetime import datetime
from aritmetica import sumar, restar, dividir, multiplicar

# El módulo 'time' servirá para que lo que se muestre en pantalla sea en un intervalo determinado de tiempo
# y no todo de golpe

def opcion2_register():
    print("¡Bienvenido a la pantalla de registro!")
    time.sleep(1)
    user()
    user_pass()
    nombre_dni()
    correo_usuario()
    fecha_nac_usuario()
    captcha()
    print("¡Felicidades! Te registraste con éxito.")

# Primero se pedirá el usuario
def user():
    while True:
        username = input("Ingresá un nombre de usuario: ")
        if len(username) < 6 or len(username) > 12:
            print("El nombre de usuario debe tener entre 6 y 12 caracteres.")
        else:
            break

# Luego la contraseña
def user_pass():
    time.sleep(0.5)
    print("Tu contraseña debe contener al menos: ")
    time.sleep(0.1)
    print("Una minúscula.")
    time.sleep(0.1)
    print("Una mayúscula.")
    time.sleep(0.1)
    print("Un número.")
    time.sleep(0.1)
    print("Un caracter especial.")
    time.sleep(0.1)
    while True:
        password = input("Ingresá una contraseña: ")
        if len(password) < 8:
            print("La contraseña debe tener al menos 8 caracteres.")

        with_numbers = any(char.isdigit()for char in password) 
        with_symbols = any(not char.isalnum()for char in password)
        with_upper = any(char.isupper()for char in password)
        with_lower = any(char.islower()for char in password)

        if with_numbers and with_symbols and with_upper and with_lower and len(password) > 8:
            print("Contraseña válida")
            break
        else:
            if not with_numbers:
                print("La contraseña debe tener al menos un número.")
            if not with_symbols:
                print("La contraseña debe contener al menos un símbolo.")
            if not with_upper:
                print("La contraseña debe tener al menos una mayúscula.")
            if not with_lower:
                print("La contraseña debe tener al menos una minúscula.")
    return password

# Luego nombre, apellido, dni
def nombre_dni():
    nombre = input("Ingresá tu nombre: ").capitalize()

    apellido = input("Ingresá tu apellido: ").capitalize()
    
    dni = int(input("Ingresá tu DNI: "))

# Su correo electrónico
def correo_usuario():    
    while True:
        correo = input("Ingresá tu correo electrónico: ")
        if "@" not in correo:
            print("Ingresá una dirección de correo válida.")
        else:
            break

#La fecha de nacimiento
def fecha_nac_usuario():  
    while True:
        fecha_nac = input("Ingresá tu fecha de nacimiento (DD-MM-AAAA): ")
        try:
            fecha_obj = datetime.strptime(fecha_nac, "%d-%m-%Y")

            dia, mes, anio = fecha_obj.day, fecha_obj.month, fecha_obj.year
            anio_actual = datetime.now().year

            if mes > 12:
                print("El mes no puede ser mayor a 12. Intentá de nuevo.")
            elif dia > 31:
                print("El día no puede ser mayor a 31. Intentá de nuevo.")
            elif anio > anio_actual:
                print("El año no puede ser mayor al actual. Intentá de nuevo.")
            else:
                break

        except ValueError:
            print("Formato incorrecto. Ingresá tu fecha de nacimiento en el formato DD-MM-AAAA")

#Finalmemte pedimos el captcha para completar el registro
def captcha():
    while True:
        funciones = [sumar, restar, dividir, multiplicar]

        funcion_operacion = random.choice(funciones)
        a = random.uniform(1.00, 10.00)
        b = random.uniform(1.00, 10.00)
        print(f"Para poder continuar, resuelva la siguiente operación: {funcion_operacion.__name__.upper()}({round(a, 2)}, {round(b, 2)})")

        resultado = float(input("Ingrese su respuesta: "))

        resultado_correcto = funcion_operacion(a, b)

        if resultado == resultado_correcto:
            print("La respuesta es correcta.")
            break
        else:
            print(f"Incorrecto. La respuesta correcta era {resultado_correcto}. Intenta de nuevo.\n")