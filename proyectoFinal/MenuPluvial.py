import pandas as pd
import os
import csv


def cargar_registros_pluviales():
    # Solicitar al usuario el año 
    año = input("Por favor, ingrese el año para cargar los registros pluviales: ")
    nombre_archivo = f'registro_pluvial_{año}.csv'
    
    # Comprobar si el archivo existe
    if os.path.exists(nombre_archivo):
        # Se cargar el DataFrame desde el archivo CSV 
        df = pd.read_csv(nombre_archivo)
        print(f"Archivo cargado: {nombre_archivo}")
        
        # Mostrar los meses disponibles 
        meses = df.columns.tolist()
        print("Meses disponibles:", meses)

        # Solicitar al usuario un mes 
        mes_elegido = input("Elige un mes: ")
        
        if mes_elegido in meses:
            # Obtener los registros del mes seleccionado 
            registros_mes = df[mes_elegido].dropna() 
            print(f"Registros de lluvia de {mes_elegido} {año}:")
            print(registros_mes)
        else:
            print(f"Mes '{mes_elegido}' no se encontro en el archivo.")
    else:
        print(f"El archivo '{nombre_archivo}' no existe. Verificar el año ingresado.")
        
# Menu de carga de registro
def main():
    while True:
        print("1. Cargar registros ")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            cargar_registros_pluviales()
        elif opcion == '2':
            print("Salir del programa.")
            break
        else:
            print("Opción no válida. Intentar de nuevo.")

if __name__ == "__main__":
    main()