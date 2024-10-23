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

# ***** Métodos de búsqueda *****

def busqueda_secuencial(usuarios, nombre_usuario):
    """Búsqueda secuencial: recorre la lista de usuarios buscando por nombre de usuario."""
    for usuario in usuarios:
        if usuario.nombre_usuario == nombre_usuario:
            print(f"Usuario encontrado: ID: {usuario.id}, Nombre de usuario: {usuario.nombre_usuario}, Email: {usuario.email}")
            return usuario
    print("Usuario no encontrado.")
    return None

def busqueda_binaria(usuarios, nombre_usuario):
    """Búsqueda binaria: requiere que la lista esté ordenada por nombre de usuario."""
    usuarios_ordenados = ordenar_usuarios(usuarios)  # Obtener la lista ordenada
    inicio = 0
    fin = len(usuarios_ordenados) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if usuarios_ordenados[medio].nombre_usuario == nombre_usuario:
            usuario = usuarios_ordenados[medio]
            print(f"Usuario encontrado: ID: {usuario.id}, Nombre de usuario: {usuario.nombre_usuario}, Email: {usuario.email}")
            return usuario
        elif usuarios_ordenados[medio].nombre_usuario < nombre_usuario:
            inicio = medio + 1
        else:
            fin = medio - 1
    
    print("Usuario no encontrado.")
    return None
def buscar_usuario(usuarios):
    """Opción principal para buscar usuario, eligiendo entre búsqueda secuencial o binaria."""
    nombre_usuario = input("Ingrese el nombre de usuario para buscar: ")
    print("\nElija el método de búsqueda:")
    print("1. Búsqueda Secuencial")
    print("2. Búsqueda Binaria")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        busqueda_secuencial(usuarios, nombre_usuario)
    elif opcion == '2':
        busqueda_binaria(usuarios, nombre_usuario)
    else:
        print("Opción de búsqueda no válida.")

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

#-----------------------------------------------------------------------
def ordenar_usuarios(usuarios):
    # Ordenar la lista de usuarios en su lugar
    usuarios.sort(key=lambda usuario: usuario.nombre_usuario)
    return usuarios

def ordenar_sort(usuarios):
    ordenar_usuarios(usuarios)  # Llama a la función que ordena
    guardar_usuarios(usuarios)    #le hago guardar el resultado ordenado
    for usuario in usuarios:
        print(f"ID: {usuario.id}, nombre de usuario: {usuario.nombre_usuario}, Email: {usuario.email}")
    
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
    guardar_usuarios(usuarios)    #le hago guardar el resultado ordenado
    for usuario in usuarios_ordenados:
        print(f"ID: {usuario.id}, nombre de usuario: {usuario.nombre_usuario}, Email: {usuario.email}")

# ********** REGISTROS PLUVIALES ****************
import pandas as pd
import numpy as np
import os
import random
import matplotlib.pyplot as plt
#--------------------------------------------------------
def generar_registros_aleatorios(año):
    # Genera registros pluviales aleatorios
    registros = []
    dias_en_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for mes in range(12):
        dias = dias_en_mes[mes]
        mes_registros = [random.randint(0, 100) for _ in range(dias)]
        registros.append(mes_registros)


    # Guardar los registros en un DataFrame y exportar a CSV
    df = pd.DataFrame(registros).T
    df.columns = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
                  'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    df.to_csv(f'registroPluvial{año}.csv', index=False)

    return df
#----------------------------------------------------------------------------------------------------
# Si no encuentra el archivo, genera uno aleatorio llamando la funcion generar_refistros-aleatorios
def cargar_registros(año):
    nombre_archivo = f'registroPluvial{año}.csv'
    
    if os.path.exists(nombre_archivo):
        df = pd.read_csv(nombre_archivo)
        print(f"Registros cargados del archivo {nombre_archivo}.")
        return df
    else:
        print(f"No se encontró el archivo. Generando informacion para el año {año}.")
        return generar_registros_aleatorios(año)
#-----------------------------------------------------------------------------------------------------
#mostrar los Registro de un mes en particular
def mostrar_registros_mes(df, mes):  #recibe dos argumentos dataFrame y nombre del mes
    meses = {
        'Enero': 0,
        'Febrero': 1,
        'Marzo': 2,
        'Abril': 3,
        'Mayo': 4,
        'Junio': 5,
        'Julio': 6,
        'Agosto': 7,
        'Septiembre': 8,
        'Octubre': 9,
        'Noviembre': 10,
        'Diciembre': 11,
    }
    
    mes_index = meses.get(mes)
    if mes_index is not None:
        print(f"Registros de {mes}:")
        # Selecciona los registros de lluvia y elimina los nulos
        registros = df.iloc[:, mes_index].dropna() #dropna elimina valores nulos
        
        # Imprime los días (índices + 1) para no mostrar un dia 0 y sus correspondientes registros
        for i, valor in enumerate(registros):
            print(f"Día {i + 1}: {valor} mm") 
    else:
        print("Mes no válido.")
#-------------------------------------------------------------------------
# ********** GENERA GRAFICAS ****************

def graficar_lluvias(df, año):
    df_sum = df.sum()
    
    # Gráfico de barras
    plt.figure(figsize=(10, 6))
    df_sum.plot(kind='bar', color='skyblue')
    plt.title(f'Precipitación Anual en el Año {año}')
    plt.xlabel('Meses')
    plt.ylabel('Milímetros')
    plt.show()
    
    # Gráfico de dispersión
    plt.figure(figsize=(10, 6))
    for i, mes in enumerate(df.columns):
        plt.scatter([i + 1] * len(df[mes]), df[mes], label=mes)
    plt.title('Dispersión de Precipitaciones')
    plt.xlabel('Meses')
    plt.ylabel('Milímetros')
    plt.xticks(range(1, 13), df.columns, rotation=45)
    plt.show()
    
    # Gráfico circular
    plt.figure(figsize=(10, 6))
    df_sum.plot(kind='pie', autopct='%1.1f%%')
    plt.title(f'Precipitación Anual por Mes en el Año {año}')
    plt.ylabel('')
    plt.show()

#*********** MENU PRINCIPAL *******************
def menu_principal():
    usuarios = cargar_usuarios() #carga en variable los usuarios
    #registros_pluviales = cargar_registros()
    print(usuarios)
    while True:
        print("\nMenú Principal")
        print("1. Agregar Usuario")
        print("2. Modificar Usuario")
        print("3. Eliminar Usuario")
        print("4. Buscar Usuario")
        print("5. Ordenar Usuarios")
        print("6. Mostrar Todos los Usuarios")
        print("7. Ingresar al Sistema")
        print("8. Mostrar registros pluviales")
        print("9. Graficar registros pluviales")
        print("10. Salir")
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
            print("Desea ordenar por metodo QUICK SORT, ingrese 1")
            print("Desea ordenar por el metodo SORT de Python, ingrese 2")
            eleccion= input("Seleccione una opcion: ")
            if eleccion =='1':
             ordenar_quick_sort(usuarios)
            else:
             ordenar_sort(usuarios)   
        elif opcion =='6':    
            mostrar_usuarios(usuarios)
        elif opcion == '7':
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
        elif opcion == '8':
             año = int(input("Ingrese el año (ej. 2023): "))
             df = cargar_registros(año)
             mes1 = input("Ingrese el mes que desea consultar (ej. Enero): ")
             mes=mes1.capitalize() #pone en mayuscula la primer letra
             mostrar_registros_mes(df, mes)

        elif opcion == '9':
             año = int(input("Ingrese el año (ej. 2023): "))
             df = cargar_registros(año)
             graficar_lluvias(df, año)       
        elif opcion == '10':
            exit()
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_principal()

