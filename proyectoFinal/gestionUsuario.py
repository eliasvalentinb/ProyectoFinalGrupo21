import pickle
from datetime import datetime
import gestionAccesos
import os
import Tienda_Online
import Vendedor_Admin

class Usuario:
    def __init__(self, id, nombre_usuario, dni, password, email):
        self._id = id
        self._nombre_usuario = nombre_usuario
        self._dni = dni
        self._password = password
        self._email = email

            # ENCAPSULAMIENTO

    # Getters
    def get_id(self):
        return self._id

    def get_nombre_usuario(self):
        return self._nombre_usuario

    def get_dni(self):
        return self._dni

    def get_password(self):
        return self._password

    def get_email(self):
        return self._email

    # Setters
    def set_nombre_usuario(self, nombre_usuario):
        self._nombre_usuario = nombre_usuario

    def set_dni(self, dni):
        self._dni = dni

    def set_password(self, password):
        self._password = password

    def set_email(self, email):
        self._email = email

"""class Acceso:
    def __init__(self, id, fechaIngreso, fechaSalida, usuarioLogueado):
        self.id = id
        self.fechaIngreso = fechaIngreso
        self.fechaSalida = fechaSalida
        self.usuarioLogueado = usuarioLogueado"""
        
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
    usuarios.sort(key=lambda usuario:int(usuario.get_dni())) #ordena por DNI
    with open('usuarios.ispc', 'wb') as file:
        pickle.dump(usuarios, file)

def guardar_usuarios_orden_username(usuarios):
    with open('usuariosOrdenadosPorUsername.ispc', 'wb') as file:
        pickle.dump(usuarios, file)

# ----------------- AGREGAR - MODIFICAR - ELIMINAR USUARIO --------------------
def agregar_usuario(usuarios):
    print("\n ---------------------")
    print("| AGREGAR NUEVO USUARIO |")
    print(" -----------------------")
    id = len(usuarios) + 1
    nombre_usuario = input("Ingrese un nombre de usuario: ")
    dni = int(input("Ingrese DNI: "))
    password = input("Ingrese una contraseña: ")
    email = input("Ingrese un correo electrónico: ")
    usuarios.append(Usuario(id, nombre_usuario,dni, password, email))
    guardar_usuarios(usuarios)
    print("¡Usuario agregado exitosamente!")

def modificar_usuario(usuarios):
    print("\n ---------------------")
    print("| MODIFICAR UN USUARIO |")
    print(" ---------------------")
    nombre_usuario = input("Ingrese el username del usuario a modificar: ")
    for usuario in usuarios:
        if usuario.get_nombre_usuario() == nombre_usuario:
            usuario.set_password() == input("Ingrese la nueva contraseña: ")
            usuario.set_email() == input("Ingrese el nuevo correo electrónico: ")
            guardar_usuarios(usuarios)
            print("¡Usuario modificado exitosamente!")
            return
    print("Usuario no encontrado.")

def eliminar_usuario(usuarios):
    print("\n ---------------------")
    print("| ELIMINAR UN USUARIO |")
    print(" ---------------------")
    nombre_usuario = input("Ingrese el username o el correo del usuario a eliminar: ")
    for usuario in usuarios:
        if usuario.get_nombre_usuario() == nombre_usuario or usuario.get_email() == nombre_usuario:
            usuarios.remove(usuario)
            guardar_usuarios(usuarios)
            print("¡Usuario eliminado exitosamente!")
            return
    print("Usuario no encontrado.")



# ---------------------- Buscar Usuarios -----------------------------------------------------

def busqueda_secuencial(usuarios, nombre_usuario,tipo):
    for intento, usuario in enumerate(usuarios, start=1):
     if tipo == "Username":
        if usuario.nombre_usuario == nombre_usuario:
            print(f"Intento {intento}: {nombre_usuario} es igual a {usuario.get_nombre_usuario()}. Se encontró en {intento} intentos.")
            print(f"Usuario encontrado: ID: {usuario.get_id()}, Nombre de usuario: {usuario.get_nombre_usuario()}, DNI: {usuario.get_dni()}, Email: {usuario.get_email()}")
            return usuario
        else:print(f"Intento {intento}: {nombre_usuario} es distinto a {usuario.get_nombre_usuario()}")
     else:  
        if usuario.get_email() == nombre_usuario:
            print(f"Intento {intento}: {nombre_usuario} es igual a {usuario.get_email()}. Se encontró en {intento} intentos.")
            print(f"Usuario encontrado: ID: {usuario.get_id()}, Nombre de usuario: {usuario.get_nombre_usuario()}, DNI: {usuario.get_dni()}, Email: {usuario.get_email()}")
            return usuario
        else:print(f"Intento {intento}: {nombre_usuario} es distinto a {usuario.get_email()}")
    print("Usuario no encontrado.")
    return None

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
        if dni_buscado < usuarios_ordenados[inicio].get_dni():
            log_file.write(f"El DNI a buscar {dni_buscado} no está en nuestra base, es inferior al menor de los DNI registrados ({usuarios_ordenados[inicio].dni}).")
            print(f"El DNI a buscar {dni_buscado} no está en nuestra base, es inferior al menor de los DNI registrados ({usuarios_ordenados[inicio].dni}).")
            return None
        elif dni_buscado > usuarios_ordenados[fin].get_dni():
            log_file.write(f"No se encuentra registrado un usuario con el DNI indicado debido a que el DNI a buscar {dni_buscado} es más grande que el más grande de los registrados: {usuarios_ordenados[fin].dni}.")
            print(f"No se encuentra registrado un usuario con el DNI indicado debido a que el DNI a buscar {dni_buscado} es más grande que el más grande de los registrados: {usuarios_ordenados[fin].dni}.")
            return None


        while inicio <= fin:
            intento += 1
            medio = (inicio + fin) // 2
            dni_medio = usuarios_ordenados[medio].get_dni()
            if dni_medio == dni_buscado:
                usuario = usuarios_ordenados[medio]
                log_file.write(f"Intento {intento} - valor buscado {dni_buscado} - valor medio {dni_medio} - Se encontro el usuario.\n")
                print(f"Se encontró el usuario en {intento} intentos: ID: {usuario.get_id()}, Nombre de usuario: {usuario.get_nombre_usuario()}, DNI: {usuario.get_dni()}, Email: {usuario.get_email()}.")
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
        if nombre_usuario < usuarios_ordenados[inicio].get_nombre_usuario():
            log_file.write(f"el usuario a buscar {nombre_usuario} no esta en base, es inferior al menor de los Usuarios registrados ({usuarios_ordenados[inicio].nombre_usuario}).")
            print(f"el usuario a buscar {nombre_usuario} no esta en base, es inferior al menor de los Usuarios registrados ({usuarios_ordenados[inicio].nombre_usuario}).")
            return None
        elif nombre_usuario > usuarios_ordenados[fin].get_nombre_usuario():
            log_file.write(f"No se encuentra registrado el usuario supera el rango.")
            print(f"No se encuentra registrado el usuario supera el rango.")
            return None


        while inicio <= fin:
            intento += 1
            medio = (inicio + fin) // 2
            dni_medio = usuarios_ordenados[medio].get_nombre_usuario()
            if dni_medio == nombre_usuario:
                usuario = usuarios_ordenados[medio]
                log_file.write(f"Intento {intento} - valor buscado {nombre_usuario} - valor medio {dni_medio} - Se encontro el usuario.\n")
                print(f"Se encontró el usuario en {intento} intentos: ID: {usuario.get_id()}, Nombre de usuario: {usuario.get_nombre_usuario()}, DNI: {usuario.get_dni()}, Email: {usuario.get_email()}.")
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
    print("\n -------------------------")   
    print("| BUSQUEDA POR USERNAME |")
    print(" ---------------------------") 
    nombre_usuario = input("Ingrese el nombre de usuario para buscar: ")
    if not os.path.exists('usuariosOrdenadosPorUsername.ispc'):
        busqueda_secuencial(usuarios, nombre_usuario,"Username")
        print("*** Se buscó por NOMBRE USUARIO con la técnica de BUSQUEDA SECUENCIAL ***")
    else:
        busqueda_binaria_username2(usuarios_username , nombre_usuario)
        print("*** Se buscó por NOMBRE USUARIO con la técnica de BUSQUEDA BINARIA ***")

def mostrar_usuarios(usuarios):
    for usuario in usuarios:
        print(f"ID: {usuario.get_id()}, \nNombre de usuario: {usuario.get_nombre_usuario()}, \nDNI:{usuario.get_dni()}, \nEmail: {usuario.get_email()}")

usuarios_username = cargar_usuarios_orden_username()
def mostrar_usuarios_orden_username(usuarios_username):
    for usuario in usuarios_username:
        print(f"ID: {usuario.get_id()}, \nNombre de usuario: {usuario.get_nombre_usuario()}, \nDNI:{usuario.get_dni()}, \nEmail: {usuario.get_email()}")
        

#---------------------------- Ordenar Usuarios ------------------------------
    
def quick_sort(usuarios):
    if len(usuarios) <= 1:
        return usuarios
    else:
        pivot = usuarios[len(usuarios) // 2]  # Elegir el pivote
        left = [usuario for usuario in usuarios if usuario._nombre_usuario < pivot._nombre_usuario]
        middle = [usuario for usuario in usuarios if usuario._nombre_usuario == pivot._nombre_usuario]
        right = [usuario for usuario in usuarios if usuario._nombre_usuario > pivot._nombre_usuario]
        return quick_sort(left) + middle + quick_sort(right)

def ordenar_quick_sort(usuarios):
    # Ordenar los usuarios por nombre de usuario usando Quick Sort
    usuarios_ordenados = quick_sort(usuarios)
    guardar_usuarios_orden_username(usuarios_ordenados)    #le hago guardar el resultado ordenado
    for usuario in usuarios_ordenados:
        print(f"ID: {usuario.get_id()}, Nombre de usuario: {usuario.get_nombre_usuario()}, DNI: {usuario.get_dni()}, Email: {usuario.get_email()}")


#------------------ 1.1. Acceder al CRUD de los usuarios en POO ---------------------------------
usuarios = cargar_usuarios() #carga en variable los usuarios
print(usuarios)

def gestionUsuario_ABM():
    print("\n ---------------------")
    print("| GESTION USUARIO ABM |")
    print(" ---------------------")
    print("1. Agregar nuevo usuario: ")
    print("2. Modificar un usuario: ")
    print("3. Eliminar un usuario: ")
    print("4. Volver al menú principal o al anterior: ")
    print(" ")
    opcion = input("Seleccione una opción: ")
    print(" ")
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
    print("\n -------------------------")   
    print("| BUSCAR- ORDENAR USUARIOS |")
    print(" ---------------------------") 
    print("1. Ordenar usuarios por Username: ")
    print("2. Buscar y mostrar usuarios: ")
    print("3. Volver al menú principal o al anterior: ")
    opcion = input("\nSeleccione una opción: ")
    if opcion =="1": #ordenar por username, crea el archivo usuariosOrdenadosPorUsername.ispc
        ordenar_quick_sort(usuarios)        #se aplica tecnica quick sort
    elif opcion =="2": #buscar y mostrar usarios
        print("\n1. Buscar usuario por dni: ")
        print("2. Buscar por username: ")
        print("3. Buscar por correo electrónico: ")
        print("4. Mostrar todos los usuarios")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            print("\n¿Qué usuario quiere buscar?: ")
            dni_usuario = int(input("\nIngrese el DNI: "))
            busqueda_binaria_dni2(usuarios, dni_usuario)
            print("*** Se buscó por DNI con la técnica de BUSQUEDA BINARIA ***")
        elif opcion == "2":
            buscar_usuario_username(usuarios)
        elif opcion == "3":
            print("\n¿Qué usuario quiere buscar?: ")
            email= input("Ingrese el correo que desea buscar: ")
            busqueda_secuencial(usuarios,email,"email")
            print("*** Se buscó por EMAIL con la técnica de BUSQUEDA SECUENCIAL ***")
        elif opcion == "4":
            print("1. Mostrar los usuarios del archivo usuarios.ispc")
            print("2. Mostar los usuarios del archivo usuariosOrdenadosPorUsername.ispc")
            opcion = input("Ingrese una opción: ")
            if opcion == "1":
                mostrar_usuarios(usuarios)
            elif opcion == "2":
                mostrar_usuarios_orden_username(usuarios_username)
            else: 
                print("Opción no válida.")
 
def usuarios_accesos():
    while True:
     print("\n -------------------")   
     print("| USUARIOS Y ACCESOS |")
     print(" --------------------") 
     print("1.Quiero realizar un ABM de usuario:")
     print("2.Quiero ver los registros de acceso:")
     print("3.Quiero buscar/ ordenar usuarios:")
     print("4.Quiero volver al Menu principal:")
     print(" ")
     opcion = input("Seleccione una opción: ")
     #REALIZA ABM
     if opcion =="1":  
      gestionUsuario_ABM() #agrega, modifica, elimina usuarios
     #VER REGISTROS DE ACCESOS  
     elif opcion == "2":
      gestionAccesos.mostrar_Accesos()
     #BUSCAR / ORDENAR USUARIO
     elif opcion == "3": 
            gestionUsuario_BO() 
     elif opcion == "4":
          break
 #-------------------------------------------------------------------------------------------
def ingresar():
            nombre_usuario = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            usuario = next((u for u in usuarios if u.get_nombre_usuario() == nombre_usuario and u.get_password() == password), None)
            if usuario:
                print("\n¡Ingreso exitoso!")
                gestionAccesos.registrar_acceso(usuario)
                """print("                  BIENVENIDO A LA TIENDA ONLINE                     ")
                print("====================================================================")
                print ("Podemos ofrecerte las siguientes opciones: ")
                print("--------------------------------------------------------------------")"""
                while True:
                    print("                  BIENVENIDO A LA TIENDA ONLINE                     ")
                    print("====================================================================")
                    print ("Podemos ofrecerte las siguientes opciones: ")
                    print("--------------------------------------------------------------------")
                    print("\n1. Realizar una Compra ")
                    print("2. Ingresar como Vendedor/Admin")
                    print("3. Volver al Menú Principal")
                    print("4. Salir")
                    print(" ")
                    sub_opcion = input("Seleccione una opción: ")
                    print(" ")
                    if sub_opcion == '1':
                        Tienda_Online.carrito(nombre_usuario)
                    elif sub_opcion == '2':
                        Vendedor_Admin.vend_adm()
                    elif sub_opcion == '3':
                        break                    
                    elif sub_opcion == '4':
                        exit()
            else:
                print("Nombre de usuario o contraseña incorrectos.")
                gestionAccesos.registrar_logueo_fallido(nombre_usuario, password)