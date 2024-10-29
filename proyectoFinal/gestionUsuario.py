import pickle
from datetime import datetime
import gestionAccesos
import os


class Usuario:
    def __init__(self, id, nombre_usuario,dni, password, email):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.dni = dni                           
        self.password = password
        self.email = email

class Acceso:
    def __init__(self, id, fechaIngreso, fechaSalida, usuarioLogueado):
        self.id = id
        self.fechaIngreso = fechaIngreso
        self.fechaSalida = fechaSalida
        self.usuarioLogueado = usuarioLogueado
        
#***********CRUD***************

def cargar_usuarios():
    try:
        with open('usuarios.ispc', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []
    
def cargar_usuarios_orden_username():
    try:
        with open('usuariosOrdenadosPorUsername.ispc', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

def guardar_usuarios(usuarios):
    usuarios.sort(key=lambda usuario:int(usuario.dni)) #ordena por DNI
    with open('usuarios.ispc', 'wb') as file:
        pickle.dump(usuarios, file)

def guardar_usuarios_orden_username(usuarios):
    with open('usuariosOrdenadosPorUsername.ispc', 'wb') as file:
        pickle.dump(usuarios, file)

# ----------------- AGREGAR - MODIFICAR - ELIMINAR USUARIO --------------------
def agregar_usuario(usuarios):
    id = len(usuarios) + 1
    nombre_usuario = input("Ingrese nombre de usuario: ")
    dni = int(input("Ingrese DNI"))
    password = input("Ingrese password: ")
    email = input("Ingrese email: ")
    usuarios.append(Usuario(id, nombre_usuario,dni, password, email))
    guardar_usuarios(usuarios)
    print("Usuario agregado exitosamente.")

def modificar_usuario(usuarios):
    nombre_usuario = input("Ingrese el nombre de usuario del usuario a modificar: ")
    for usuario in usuarios:
        if usuario.nombre_usuario == nombre_usuario:
            usuario.password = input("Ingrese nuevo password: ")
            usuario.email = input("Ingrese nuevo email: ")
            guardar_usuarios(usuarios)
            print("Usuario modificado exitosamente.")
            return
    print("Usuario no encontrado.")

def eliminar_usuario(usuarios):
    nombre_usuario = input("Ingrese el nombre de usuario o email del usuario a eliminar: ")
    for usuario in usuarios:
        if usuario.nombre_usuario == nombre_usuario or usuario.email == nombre_usuario:
            usuarios.remove(usuario)
            guardar_usuarios(usuarios)
            print("Usuario eliminado exitosamente.")
            return
    print("Usuario no encontrado.")



# ---------------------- Buscar Usuarios -----------------------------------------------------

def busqueda_secuencial(usuarios, nombre_usuario,tipo):
    for intento, usuario in enumerate(usuarios, start=1):
     if tipo == "Username":
        if usuario.nombre_usuario == nombre_usuario:
            print(f"Intento {intento}: {nombre_usuario} es igual a {usuario.nombre_usuario}. Se encontró en {intento} intentos.")
            print(f"Usuario encontrado: ID: {usuario.id}, Nombre de usuario: {usuario.nombre_usuario}, DNI: {usuario.dni}, Email: {usuario.email}")
            return usuario
        else:print(f"Intento {intento}: {nombre_usuario} es distinto a {usuario.nombre_usuario}")
     else:  
        if usuario.email == nombre_usuario:
            print(f"Intento {intento}: {nombre_usuario} es igual a {usuario.email}. Se encontró en {intento} intentos.")
            print(f"Usuario encontrado: ID: {usuario.id}, Nombre de usuario: {usuario.nombre_usuario}, DNI: {usuario.dni}, Email: {usuario.email}")
            return usuario
        else:print(f"Intento {intento}: {nombre_usuario} es distinto a {usuario.email}")
    print("Usuario no encontrado.")
    return None

"""def busqueda_binaria_dni(usuarios, nombre_usuario):
    usuarios_ordenados = usuarios  
    inicio = 0
    fin = len(usuarios_ordenados) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if usuarios_ordenados[medio].dni == nombre_usuario:
            usuario = usuarios_ordenados[medio]
            print(f"Usuario encontrado: ID: {usuario.id}, Nombre de usuario: {usuario.nombre_usuario},DNI: {usuario.dni}, Email: {usuario.email}")
            return usuario
        elif usuarios_ordenados[medio].dni < nombre_usuario:
            inicio = medio + 1
        else:
            fin = medio - 1
    
    print("Usuario no encontrado.")
    return None"""


def busqueda_binaria_dni2(usuarios, dni_buscado):
    
    usuarios_ordenados = usuarios
    inicio = 0
    fin = len(usuarios_ordenados) - 1
    intento = 0

    fecha = datetime.now().strftime("%Y%m%d-%Hh%Mm") #guarda la fecha para el nombre del archivo log
    os.makedirs("BusquedayOrdenamiento", exist_ok=True) #valida si existe al carpeta, sino la crea
    ruta = os.path.join("BusquedayOrdenamiento", f"buscandoUsuarioPorDNI-{fecha}.txt")
    with open( ruta, 'w') as log_file:

    # se valida si esta dentro de los DNI existentes
        if dni_buscado < usuarios_ordenados[inicio].dni:
            log_file.write(f"el DNI a buscar {dni_buscado} no esta en base, es inferior al menor de los DNI registrados ({usuarios_ordenados[inicio].dni}).")
            print(f"el DNI a buscar {dni_buscado} no esta en base, es inferior al menor de los DNI registrados ({usuarios_ordenados[inicio].dni}).")
            return None
        elif dni_buscado > usuarios_ordenados[fin].dni:
            log_file.write(f"No se encuentra registrado el usuario con ese DNI debido a que el DNI a buscar {dni_buscado} es más grande que el más grande de los registrados: {usuarios_ordenados[fin].dni}.")
            print(f"No se encuentra registrado el usuario con ese DNI debido a que el DNI a buscar {dni_buscado} es más grande que el más grande de los registrados: {usuarios_ordenados[fin].dni}.")
            return None


        while inicio <= fin:
            intento += 1
            medio = (inicio + fin) // 2
            dni_medio = usuarios_ordenados[medio].dni
            if dni_medio == dni_buscado:
                usuario = usuarios_ordenados[medio]
                log_file.write(f"Intento {intento} - valor buscado {dni_buscado} - valor medio {dni_medio} - Se encontro el usuario.\n")
                print(f"Se encontró el usuario en {intento} intentos: ID: {usuario.id}, Nombre de usuario: {usuario.nombre_usuario}, DNI: {usuario.dni}, Email: {usuario.email}.")
                return usuario
            elif dni_medio < dni_buscado:
                log_file.write(f"Intento {intento} - valor buscado {dni_buscado} - valor medio {dni_medio} - Se busca a la derecha.\n")
                inicio = medio + 1
            else:
                log_file.write(f"Intento {intento} - valor buscado {dni_buscado} - valor medio {dni_medio} - Se busca a la izquierda.\n")
                fin = medio - 1
    log_file.write(f"Se realizaron {intento} intentos y no se encontró el DNI buscado, no está registrado.\n") 
    print(f"Se realizaron {intento} intentos y no se encontró el DNI buscado, no está registrado.")
    return None


"""def busqueda_binaria_username(usuarios, nombre_usuario):
    usuarios_ordenados = usuarios 
    inicio = 0
    fin = len(usuarios_ordenados) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if usuarios_ordenados[medio].nombre_usuario == nombre_usuario:
            usuario = usuarios_ordenados[medio]
            print(f"Usuario encontrado: ID: {usuario.id}, Nombre de usuario: {usuario.nombre_usuario},DNI: {usuario.dni}, Email: {usuario.email}")
            return usuario
        elif usuarios_ordenados[medio].nombre_usuario < nombre_usuario:
            inicio = medio + 1
        else:
            fin = medio - 1
    
    print("Usuario no encontrado.")
    return None"""

def busqueda_binaria_username2(usuarios_username, nombre_usuario):
    usuarios_ordenados = usuarios_username
    inicio = 0
    fin = len(usuarios_ordenados) - 1
    intento = 0

    fecha = datetime.now().strftime("%Y%m%d-%Hh%Mm") #guarda la fecha para el nombre del archivo log
    os.makedirs("BusquedayOrdenamiento", exist_ok=True) #valida si existe al carpeta, sino la crea
    ruta = os.path.join("BusquedayOrdenamiento", f"buscandoUsuarioPorUsuario-{fecha}.txt")
    with open( ruta, 'w') as log_file:

    # se valida si esta dentro de los DNI existentes
        if nombre_usuario < usuarios_ordenados[inicio].nombre_usuario:
            log_file.write(f"el usuario a buscar {nombre_usuario} no esta en base, es inferior al menor de los Usuarios registrados ({usuarios_ordenados[inicio].nombre_usuario}).")
            print(f"el usuario a buscar {nombre_usuario} no esta en base, es inferior al menor de los Usuarios registrados ({usuarios_ordenados[inicio].nombre_usuario}).")
            return None
        elif nombre_usuario > usuarios_ordenados[fin].nombre_usuario:
            log_file.write(f"No se encuentra registrado el usuario supera el rango.")
            print(f"No se encuentra registrado el usuario supera el rango.")
            return None


        while inicio <= fin:
            intento += 1
            medio = (inicio + fin) // 2
            dni_medio = usuarios_ordenados[medio].nombre_usuario
            if dni_medio == nombre_usuario:
                usuario = usuarios_ordenados[medio]
                log_file.write(f"Intento {intento} - valor buscado {nombre_usuario} - valor medio {dni_medio} - Se encontro el usuario.\n")
                print(f"Se encontró el usuario en {intento} intentos: ID: {usuario.id}, Nombre de usuario: {usuario.nombre_usuario}, DNI: {usuario.dni}, Email: {usuario.email}.")
                return usuario
            elif dni_medio < nombre_usuario:
                log_file.write(f"Intento {intento} - valor buscado {nombre_usuario} - valor medio {dni_medio} - Se busca a la derecha.\n")
                inicio = medio + 1
            else:
                log_file.write(f"Intento {intento} - valor buscado {nombre_usuario} - valor medio {dni_medio} - Se busca a la izquierda.\n")
                fin = medio - 1
    log_file.write(f"Se realizaron {intento} intentos y no se encontró el Usuario buscado, no está registrado.\n") 
    print(f"Se realizaron {intento} intentos y no se encontró el DNI buscado, no está registrado.")
    return None

# -- buscar usuario por UserName

def buscar_usuario_username(usuarios):
    nombre_usuario = input("Ingrese el nombre de usuario para buscar: ")
    if not os.path.exists('usuariosOrdenadosPorUsername.ispc'):
        busqueda_secuencial(usuarios, nombre_usuario,"Username")
        print("*** Se buscó por NOMBRE USUARIO con la técnica de BUSQUEDA SECUENCIAL ***")
    else:
        busqueda_binaria_username2(usuarios_username , nombre_usuario)
        print("*** Se buscó por NOMBRE USUARIO con la técnica de BUSQUEDA BINARIA ***")

def mostrar_usuarios(usuarios):
    for usuario in usuarios:
        print(f"ID: {usuario.id}, nombre de usuario: {usuario.nombre_usuario},DNI:{usuario.dni}, Email: {usuario.email}")

usuarios_username = cargar_usuarios_orden_username()
def mostrar_usuarios_orden_username(usuarios_username):
    for usuario in usuarios_username:
        print(f"ID: {usuario.id}, nombre de usuario: {usuario.nombre_usuario},DNI:{usuario.dni}, Email: {usuario.email}")
        

#---------------------------- Ordenar Usuarios ------------------------------
"""def ordenar_usuarios(usuarios):
    # Ordenar la lista de usuarios en su lugar
    usuarios.sort(key=lambda usuario: usuario.nombre_usuario)
    with open('usuariosOrdenadosPorUsername.ispc', 'wb') as file:
        pickle.dump(usuarios, file)
    return usuarios

def ordenar_sort(usuarios):
    ordenar_usuarios(usuarios)  # Llama a la función que ordena
    guardar_usuarios(usuarios)    #le hago guardar el resultado ordenado
    for usuario in usuarios:
        print(f"ID: {usuario.id}, nombre de usuario: {usuario.nombre_usuario}, Email: {usuario.email}")"""
    
def quick_sort(usuarios):
    if len(usuarios) <= 1:
        return usuarios
    else:
        pivot = usuarios[len(usuarios) // 2]  # Elegir el pivote
        left = [usuario for usuario in usuarios if usuario.nombre_usuario < pivot.nombre_usuario]
        middle = [usuario for usuario in usuarios if usuario.nombre_usuario == pivot.nombre_usuario]
        right = [usuario for usuario in usuarios if usuario.nombre_usuario > pivot.nombre_usuario]
        return quick_sort(left) + middle + quick_sort(right)

def ordenar_quick_sort(usuarios):
    # Ordenar los usuarios por nombre de usuario usando Quick Sort
    usuarios_ordenados = quick_sort(usuarios)
    guardar_usuarios_orden_username(usuarios_ordenados)    #le hago guardar el resultado ordenado
    for usuario in usuarios_ordenados:
        print(f"ID: {usuario.id}, nombre de usuario: {usuario.nombre_usuario},dni: {usuario.dni}, Email: {usuario.email}")


#------------------ 1.1. Acceder al CRUD de los usuarios en POO ---------------------------------
usuarios = cargar_usuarios() #carga en variable los usuarios
print(usuarios)

def gestionUsuario_ABM():
    print("1. Agregar Nuevo usuario: ")
    print("2. Modificar un usuario: ")
    print("3. Eliminar un usuario: ")
    print("4. Volver al menú principal o al anterior: ")
    opcion = input("Seleccione una opción: ")

    if opcion =="1":
        agregar_usuario(usuarios)
    elif opcion =="2":
        modificar_usuario(usuarios)
    elif opcion =="3":
         eliminar_usuario(usuarios)
    elif opcion == "4":
          exit()# VOLVER AL MENU PRINCIPAL/ ANTERIOR  

#------------------ 1.3. Buscar - Ordenar ---------------------------------

def gestionUsuario_BO():
    print("1. Ordenar Usuarios por Username: ")
    print("2. Buscar y Mostrar Usuarios: ")
    print("3. Volver al menú principal o al anterior: ")
    opcion = input("Seleccione una opción: ")
    if opcion =="1": #ordenar por username, crea el archivo usuariosOrdenadosPorUsername.ispc
        ordenar_quick_sort(usuarios)        #se aplica tecnica quick sort
    elif opcion =="2": #buscar y mostrar usarios
        print("1. buscar usuario por dni: ")
        print("2. Buscar usuario por username: ")
        print("3. buscar usuario por email: ")
        print("4. mostrar todos los usuarios")
        opcion = input("ingrese una opcion: ")
        if opcion == "1":
            print("Que usuario quiere buscar:")
            dni_usuario = int(input("ingrese el DNI: "))
            busqueda_binaria_dni2(usuarios, dni_usuario)
            print("*** Se buscó por DNI con la técnica de BUSQUEDA BINARIA ***")
        elif opcion == "2":
            buscar_usuario_username(usuarios)
        elif opcion == "3":
            print("Que usuario quiere buscar:")
            email= input("Ingrese el Email que desa buscar: ")
            busqueda_secuencial(usuarios,email,"email")
            print("*** Se buscó por EMAIL con la técnica de BUSQUEDA SECUENCIAL ***")
        elif opcion == "4":
            print("1. Mostrar los usuarios del archivo usuarios.ispc")
            print("2. Mostar los usuarios del archivo usuariosOrdenadosPorUsername.ispc")
            opcion = input("ingrese una opcion: ")
            if opcion == "1":
                mostrar_usuarios(usuarios)
            elif opcion == "2":
                mostrar_usuarios_orden_username(usuarios_username)
            else: 
                print("opcion invalida")
 

 #-------------------------------------------------------------------------------------------
def ingresar():
            nombre_usuario = input("Ingrese nombre de usuario: ")
            password = input("Ingrese password: ")
            usuario = next((u for u in usuarios if u.nombre_usuario == nombre_usuario and u.password == password), None)
            if usuario:
                print("Ingreso exitoso.")
                gestionAccesos.registrar_acceso(usuario)
                while True:
                    print("\n1. Volver al Menú Principal")
                    print("2. Salir")
                    sub_opcion = input("Seleccione una opción: ")
                    if sub_opcion == '1':
                        break
                    elif sub_opcion == '2':
                        exit()
            else:
                print("Nombre de usuario o password incorrectos.")
                gestionAccesos.registrar_logueo_fallido(nombre_usuario, password)