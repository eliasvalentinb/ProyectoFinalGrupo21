
import pickle
from datetime import datetime
import gestionUsuario 

class Acceso:
    def __init__(self, id, fechaIngreso, fechaSalida, usuarioLogueado):
        self.id = id
        self.fechaIngreso = fechaIngreso
        self.fechaSalida = fechaSalida
        self.usuarioLogueado = usuarioLogueado

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


def cargar_logs():
    try:
        with open('logs.txt', 'r', encoding='utf-8') as file:
            accesos = file.readlines()  # Lee todas las líneas del archivo
            # Opcional: elimina los saltos de línea y espacios en blanco
            return [linea.strip() for linea in accesos]
    except FileNotFoundError:
        return []

#--------------------------1.2 Menu Mostrar los datos de acceso--------------------------------------------------------
def mostrar_Accesos():
    print("1. Mostrar los Accesos (datos de accesos.ispc)")
    print("2. Mostrar los logs de intentos fallidos (datos de logs.txt)")
    print("3. Volver al Menú principal")
    eleccion = input("ingrese una opcion: ")
    if eleccion == "1":
        accesos = cargar_accesos()
        for acceso in accesos:
            print(f"ID:{acceso.id},Fecha Ingreso:{acceso.fechaIngreso},Fecha Salida:{acceso.fechaSalida},nombre de usuario:{acceso.usuarioLogueado}")
    elif eleccion == "2":
        logs = cargar_logs()
        for lg in logs:
            print(lg)
            #print(f"ID: {usuario.id}, nombre de usuario: {usuario.nombre_usuario}, Email: {usuario.email}")
    elif eleccion =="3":
         exit()
    else: print("Opcion no válida")