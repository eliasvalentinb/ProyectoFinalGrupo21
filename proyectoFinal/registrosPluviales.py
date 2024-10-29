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
        mes_registros = np.round(np.random.rand(dias) * 100, 2)
        registros.append(mes_registros)
    # Guardar los registros en un DataFrame y exportar a CSV
    df = pd.DataFrame(registros).T
    df.columns = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
                  'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    df.to_csv(f'registroPluvial{año}.csv', index=False)
    return df
    
#----------------------------------------------------------------------------------------------------
# Si no encuentra el archivo, genera uno aleatorio llamando la funcion generar_registros-aleatorios
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

def mostrar_registros_mes1(df, mes):  # recibe dos argumentos: dataFrame y nombre del mes
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
        registros = df.iloc[:, mes_index].dropna()  # dropna elimina valores nulos
        
        # Acumula los registros en una lista
        resultados = [f"Día {i + 1}: {valor} mm" for i, valor in enumerate(registros)]
        
        # Imprime los resultados en una sola línea
        print(" | ".join(resultados))
    else:
        print("Mes no válido.")

def graficar_lluvias2(df, año):
    df_sum = df.sum()
    
    # Crear figura y ejes
    fig, axs = plt.subplots(2, 2, figsize=(15, 12))  # 2 fila, 2 columnas
    axs = axs.flatten()  # Aplanar el array de ejes para facilitar el acceso
    # Gráfico de barras
    axs[0].bar(df.columns, df_sum, color='skyblue')
    axs[0].set_title(f'Precipitación Anual en el Año {año}')
    axs[0].set_xlabel('Meses', fontsize=12)
    axs[0].set_ylabel('Milímetros')
    axs[0].set_xticklabels(df.columns, rotation=45)
    
    # Gráfico de dispersión
  
    for i, mes in enumerate(df.columns):
        axs[1].scatter([i + 1] * len(df[mes]), df[mes], label=mes)
    axs[1].set_title('Dispersión de Precipitaciones')
    axs[1].set_xlabel('Meses')
    axs[1].set_ylabel('Milimetros')
    axs[1].set_xticks(range(1, 13))
    axs[1].set_xticklabels(df.columns, rotation=45)
   

    # Gráfico circular
    axs[2].pie(df_sum, labels=df.columns, autopct='%1.1f%%')
    axs[2].set_title(f'Precipitación Anual por Mes en el Año {año}')
    
    #plt.tight_layout()  # Ajustar el espaciado
    #plt.show()

    #graficos de Burbujas
    dias = range(1, 32)  # Rango de días del mes
    meses = df.columns
    x = []  # Lista para meses
    y = []  # Lista para días
    s = []  # Lista para tamaños de las burbujas (milímetros de lluvia)

    for i, mes in enumerate(meses):
        for dia in dias:
            if dia <= len(df[mes]):
                valor = df[mes].iloc[dia - 1]
                if not pd.isna(valor):  # Verifica que no sea nulo
                    x.append(i + 1)  # Meses en el eje x
                    y.append(dia)  # Días en el eje y
                    s.append(valor * 10)  # Tamaño de la burbuja, multiplicado por un factor para mayor visibilidad

    # Crear el gráfico de burbuja
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, s=s, alpha=0.5, edgecolors="w", linewidth=2)
    plt.title('Gráfico de Burbuja de Precipitaciones')
    plt.xlabel('Meses')
    plt.ylabel('Días')
    plt.xticks(range(1, 13), meses, rotation=45)
    plt.xlim(0.5, 12.5)  # Ajustar límites del eje x para centrar las etiquetas
    plt.ylim(0.5, 31.5)  # Ajustar límites del eje y para centrar las etiquetas
    #plt.grid(True)
    plt.tight_layout()  # Ajustar el espaciado
    plt.show()

def graficar_lluvias3(df, año):
    df_sum = df.sum()
    
    # Crear figura y ejes (2 filas, 2 columnas)
    fig, axs = plt.subplots(2, 2, figsize=(15, 12))  # 2 filas, 2 columnas
    axs = axs.flatten()  # Aplanar el array de ejes para facilitar el acceso
    
    # Gráfico de barras
    axs[0].bar(df.columns, df_sum, color='skyblue')
    axs[0].set_title(f'Precipitación Anual en el Año {año}', fontsize=12)
    axs[0].set_xlabel('Meses', fontsize=12)
    axs[0].set_ylabel('Milímetros', fontsize=12)
    axs[0].set_xticklabels(df.columns, rotation=45)

    # Gráfico de dispersión
    for i, mes in enumerate(df.columns):
        valores_mes = df[mes].dropna()
        axs[1].scatter([i + 1] * len(valores_mes), valores_mes, label=mes)
    axs[1].set_title('Dispersión de Precipitaciones', fontsize=12)
    axs[1].set_xlabel('Meses', fontsize=12)
    axs[1].set_ylabel('Milímetros', fontsize=12)
    axs[1].set_xticks(range(1, 13))
    axs[1].set_xticklabels(df.columns, rotation=45)

    # Gráfico circular
    axs[2].pie(df_sum, labels=df.columns, autopct='%1.1f%%')
    axs[2].set_title(f'Precipitación Anual por Mes en el Año {año}', fontsize=12)

    # Gráfico de burbujas
    dias = range(1, 32)  # Rango de días del mes
    meses = df.columns
    x = []  # Lista para meses
    y = []  # Lista para días
    s = []  # Lista para tamaños de las burbujas (milímetros de lluvia)

    for i, mes in enumerate(meses):
        for dia in dias:
            if dia <= len(df[mes]):
                valor = df[mes].iloc[dia - 1]
                if not pd.isna(valor):  # Verifica que no sea nulo
                    x.append(i + 1)  # Meses en el eje x
                    y.append(dia)  # Días en el eje y
                    s.append(valor * 10)  # Tamaño de la burbuja, multiplicado por un factor para mayor visibilidad

    # Crear el gráfico de burbujas
    axs[3].scatter(x, y, s=s, alpha=0.5, edgecolors="w", linewidth=2)
    axs[3].set_title('Gráfico de Burbuja de Precipitaciones', fontsize=12)
    axs[3].set_xlabel('Meses', fontsize=12)
    axs[3].set_ylabel('Días', fontsize=12)
    axs[3].set_xticks(range(1, 13))
    axs[3].set_xticklabels(meses, rotation=45)
    axs[3].set_xlim(0.5, 12.5)  # Ajustar límites del eje x para centrar las etiquetas
    axs[3].set_ylim(0.5, 31.5)  # Ajustar límites del eje y para centrar las etiquetas

    plt.tight_layout()  # Ajustar el espaciado
    plt.show()


def registrosPluviales():
    
    print("Que año quiere analizar")
    año = int(input("Ingrese el año (ej. 2023): "))
    df = cargar_registros(año)
    
    mes1 = input("Ingrese el mes que desea consultar (ej. Enero): ")
    mes = mes1.capitalize() #pone en mayuscula la primer letra
    mostrar_registros_mes(df, mes)
    
    graficar_lluvias2(df, año)
    #graficar_burbuja(df)

def main():
    año = int(input("Ingrese el año (ej. 2023): "))
    df = cargar_registros(año)
    
    mes1 = input("Ingrese el mes que desea consultar (ej. Enero): ")
    mes = mes1.capitalize() #pone en mayuscula la primer letra
    mostrar_registros_mes(df, mes)
    
    graficar_lluvias3(df, año)
    #graficar_burbuja(df)
if __name__ == "__main__":
    main()