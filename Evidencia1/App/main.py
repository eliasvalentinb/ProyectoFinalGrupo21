#En este módulo se controlara el flujo principal del programa

from register import opcion2_register

print("¡Bienvenido a la aplicación!")
print("Pulse 1 para ingresar: ")
print("Pulse 2 para registrarse: ")

#Definimos un diccionario con dos usuarios de prueba y sus respectivas contraseñas
users = {"elias18": "Hola$oy_3lias", "sofia23": "Hol4soy_$ofi"}

opcion = input("Ingresá una opción: ")

#Definimos la función para el logueo del usuario
def opcion1_login():
    #Definimos un contador para los intentos de logueo
    suma = 0
    while True: 
        user = input("Ingresá tu nombre de usuario: ")
        if user not in users:
            print("Usuario incorrecto. Intentá de nuevo.")
        else:
            break
    while suma != 4:
        password = input("Ingresá tu constraseña: ")
        if password not in users.values():
            print("La contraseña es incorrecta. Intentá de nuevo.")
            #Cada que el usuario ingrese mal la contraseña, se suma un intento al contador
            suma = suma + 1
            if suma == 2:
                print("Segundo intento fallido, al cuarto intento fallido se bloqueará la cuenta.")
            elif suma == 3:
                print("Tercer intento fallido, al cuarto intento fallido se bloqueará la cuenta.")
                #Cuando llega al cuarto intento, se le da mensaje de bloqueo y termina el programa
            elif suma == 4:
                print("Cuarto intento fallido, se ha bloqueado el acceso.")
                return
        else:
            break
        #Si los datos están bien se dará el siguiente mensaje:
    print("¡Usuario ingresado con éxito!")

if opcion == "1":
    opcion1_login()
elif opcion == "2":
    opcion2_register()
else:
    print("Ingresá una opción válida.")
