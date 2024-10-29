
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def main():

    global year
    year = None
    while True:
        print("\nMENÚ PRINCIPAL")
        print("\nAnálisis de Datos Pluviales:")
        print("1. Análisis anual")
        print("2. Análisis de un mes específico")
        print("3. Volver al Menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            year = analisis_anual()
        elif opcion == '2':
            if not year:
                year = input("Ingrese el año para el análisis mensual: ")
            elegir_mes_analizar(year)
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def generar_datos_pluviales_ano(nombre_archivo):
    # Generar datos aleatorios para un año completo (365 días)
    np.random.seed(42)
    precipitaciones = np.round(np.random.rand(365) * 100, 2)

    # Ajustar los datos para tener la cantidad correcta de días por mes
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    columnas = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    
    datos_anuales = {}
    inicio = 0
    for mes, dias in zip(columnas, dias_por_mes):
        datos_anuales[mes] = precipitaciones[inicio:inicio + dias]
        inicio += dias

    # Crear un DataFrame con los datos generados
    df_precipitaciones = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in datos_anuales.items()]))

    # Guardar el DataFrame como un archivo CSV
    df_precipitaciones.to_csv(nombre_archivo, index=False)
    print(f"Se generó el archivo '{nombre_archivo}' con datos aleatorios.")

def generar_datos_aleatorios(year):
    # Generar datos aleatorios para un año completo (365 días)
    np.random.seed(42)
    precipitaciones = np.round(np.random.rand(365) * 100, 2)

    # Ajustar los datos para tener la cantidad correcta de días por mes
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    columnas = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    
    datos_anuales = {}
    inicio = 0
    for mes, dias in zip(columnas, dias_por_mes):
        datos_anuales[mes] = precipitaciones[inicio:inicio + dias]
        inicio += dias

    # Crear un DataFrame con los datos generados
    df_precipitaciones = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in datos_anuales.items()]))

    # Guardar el DataFrame como un archivo CSV
    os.makedirs('datosGenerados', exist_ok=True)
    df_precipitaciones.to_csv(f'datosGenerados/registro_pluvial_{year}.csv', index=False)
    print(f"Se generaron y guardaron los datos aleatorios para el año {year}.")

    return df_precipitaciones

def analisis_anual():
    # Pedir al usuario que ingrese el año para el análisis
    year = input("Ingrese el año para el análisis anual: ")
    archivo_datos = f'datosGenerados/registro_pluvial_{year}.csv'

    # Verificar si ya existen datos para el año
    if os.path.exists(archivo_datos):
        print(f"Se encontraron datos existentes para el año {year}. Cargando datos...")
        df = pd.read_csv(archivo_datos)
    else:
        print(f"No se encontraron datos para el año {year}. Generando datos aleatorios...")
        df = generar_datos_aleatorios(year)

    # Crear la carpeta 'datosAnalizados' si no existe
    os.makedirs('datosAnalizados', exist_ok=True)

    # Mostrar estadísticas anuales
    max_precip = df.max().max()  # Máximo de todo el año
    min_precip = df.min().min()  # Mínimo de todo el año
    avg_precip = df.mean().mean()  # Promedio de todo el año

    print(f"\nAnálisis Anual de Precipitaciones para el año {year}:")
    print(f"Máxima precipitación anual: {max_precip}")
    print(f"Mínima precipitación anual: {min_precip}")
    print(f"Promedio de precipitación anual: {avg_precip}")

    # Gráfico de barras de las precipitaciones anuales
    df.sum().plot(kind='bar', figsize=(10, 6), title=f'Precipitación Total por Mes en {year}')
    plt.xlabel('Mes')
    plt.ylabel('Precipitación Total')
    plt.savefig(f'datosAnalizados/precipitacion_anual_{year}.png')
    plt.show()

    # Gráfico de dispersión de precipitaciones anuales
    plt.figure(figsize=(10, 6))
    for mes in df.columns:
        plt.scatter([mes] * len(df), df[mes], label=mes)
    plt.title(f'Dispersión de Precipitaciones Anuales en {year}')
    plt.xlabel('Mes')
    plt.ylabel('Precipitación')
    plt.savefig(f'datosAnalizados/dispersion_anual_{year}.png')
    plt.show()

    # Gráfico circular de distribución anual
    df.sum().plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8), title=f'Distribución Anual de Precipitaciones en {year}')
    plt.savefig(f'datosAnalizados/distribucion_anual_{year}.png')
    plt.show()

def elegir_mes_analizar(year=None):
    if not year:
        # Si el año no está definido, preguntar al usuario
        year = input("Ingrese el año para el análisis del mes: ")

    nombre_archivo = f'registro_pluvial_{year}.csv'

    if not os.path.exists(nombre_archivo):
        print(f"No se encontró el archivo '{nombre_archivo}'. Se generarán datos aleatorios para el año {year}.")
        generar_datos_pluviales_ano(nombre_archivo)

    try:
        df = pd.read_csv(nombre_archivo)
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                 "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

        for idx, mes in enumerate(meses, start=1):
            print(f"{idx}. {mes}")

        opcion = int(input("Seleccione el mes a analizar (1-12): "))
        if 1 <= opcion <= 12:
            mes_seleccionado = meses[opcion - 1]
            print(f"\nAnálisis de {mes_seleccionado} en {year}:")
            analisis_mes(df, mes_seleccionado)
        else:
            print("Opción no válida. Por favor, ingrese un número entre 1 y 12.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
    except FileNotFoundError:
        print(f"No se encontró el archivo de registros pluviales para el año {year}.")

def analisis_mes(df, mes):
    try:
        registros_mes = df[mes]

        # Limpiar valores NaN
        registros_mes = registros_mes.dropna()

        print(f"\nRegistros pluviales de {mes}:")
        print(registros_mes)
        print(f"Máxima precipitación en {mes}: {registros_mes.max()}")
        print(f"Mínima precipitación en {mes}: {registros_mes.min()}")
        print(f"Promedio de precipitación en {mes}: {registros_mes.mean()}")
        
        # Generar el gráfico circular para el mes seleccionado
        if not registros_mes.empty:
            plt.figure(figsize=(8, 8))
            plt.pie(registros_mes, labels=[f"Día {i+1}" for i in range(len(registros_mes))],
                    autopct='%1.1f%%')
            plt.title(f"Distribución de precipitaciones en {mes} en {df.columns[0]}")
            plt.savefig(f'datosAnalizados/grafico_{mes}_{df.columns[0]}.png')
            plt.show()
        else:
            print(f"No hay datos disponibles para el mes de {mes}.")
    except KeyError:
        print(f"No hay registros disponibles para el mes de {mes}.")

if __name__ == "__main__":
    main()