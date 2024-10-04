import pickle
from datetime import datetime

class Usuario:
    def __init__(self, id, nombre_usuario, password, email):
        self.id = id
        self.nombre_usuario = nombre_usuario
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

def guardar_usuarios(usuarios):
    with open('usuarios.ispc', 'wb') as file:
        pickle.dump(usuarios, file)

def agregar_usuario(usuarios):
    id = len(usuarios) + 1
    nombre_usuario = input("Ingrese nombre de usuario: ")
    password = input("Ingrese password: ")
    email = input("Ingrese email: ")
    usuarios.append(Usuario(id, nombre_usuario, password, email))
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

def buscar_usuario(usuarios):
    nombre_usuario = input("Ingrese el nombre de usuario o email del usuario a buscar: ")
    for usuario in usuarios:
        if usuario.nombre_usuario == nombre_usuario or usuario.email == nombre_usuario:
            print(f"ID: {usuario.id}, nombre de usuario: {usuario.nombre_usuario}, Email: {usuario.email}")
            return
    print("Usuario no encontrado.")

def mostrar_usuarios(usuarios):
    for usuario in usuarios:
        print(f"ID: {usuario.id}, nombre de usuario: {usuario.nombre_usuario}, Email: {usuario.email}")
        
        
#*******ACCESO Y REGISTRO*******

def registrar_acceso(usuario):
    accesos = cargar_accesos()
    id = len(accesos) + 1
    fechaIngreso = datetime.now()
    fechaSalida = None
    accesos.append(Acceso(id, fechaIngreso, fechaSalida, usuario.nombre_usuario))
    guardar_accesos(accesos)

def cargar_accesos():
    try:
        with open('accesos.ispc', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

def guardar_accesos(accesos):
    with open('accesos.ispc', 'wb') as file:
        pickle.dump(accesos, file)

def registrar_logueo_fallido(nombre_usuario, password):
    with open('logs.txt', 'a') as file:
        file.write(f"{datetime.now()} - nombre de usuario: {nombre_usuario}, Password: {password}\n")
        
#*********** MENU PRINCIPAL *******************
def menu_principal():
    usuarios = cargar_usuarios()
    while True:
        print("\nMenú Principal")
        print("1. Agregar Usuario")
        print("2. Modificar Usuario")
        print("3. Eliminar Usuario")
        print("4. Buscar Usuario")
        print("5. Mostrar Todos los Usuarios")
        print("6. Ingresar al Sistema")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_usuario(usuarios)
        elif opcion == '2':
            modificar_usuario(usuarios)
        elif opcion == '3':
            eliminar_usuario(usuarios)
        elif opcion == '4':
            buscar_usuario(usuarios)
        elif opcion == '5':
            mostrar_usuarios(usuarios)
        elif opcion == '6':
            nombre_usuario = input("Ingrese nombre de usuario: ")
            password = input("Ingrese password: ")
            usuario = next((u for u in usuarios if u.nombre_usuario == nombre_usuario and u.password == password), None)
            if usuario:
                print("Ingreso exitoso.")
                registrar_acceso(usuario)
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
                registrar_logueo_fallido(nombre_usuario, password)
        elif opcion == '7':
            exit()
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_principal()

    