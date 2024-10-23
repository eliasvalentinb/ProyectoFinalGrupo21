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
def mostrar_registros_mes(df, mes): #recibe dos argumentos dataFrame y nombre del mes
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

def main():
    año = int(input("Ingrese el año (ej. 2023): "))
    df = cargar_registros(año)
    
    mes1 = input("Ingrese el mes que desea consultar (ej. Enero): ")
    mes = mes1.capitalize() #pone en mayuscula la primer letra
    mostrar_registros_mes(df, mes)
    
    graficar_lluvias(df, año)

if __name__ == "__main__":
    main()
