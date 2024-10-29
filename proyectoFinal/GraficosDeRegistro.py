import csv
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt


# Definir los nombres de los meses
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
         'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

# Definir la cantidad de días en cada mes (sin bisiesto)
dias_por_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Crear un diccionario para almacenar los registros de lluvias de cada mes
registro_pluvial = {}

for mes, dias in zip(meses, dias_por_mes):
    # Generar lluvias aleatorias para cada día del mes (entre 0 y 100 mm)
    registro_pluvial[mes] = [round(random.uniform(0, 100), 2) for _ in range(dias)]

# Crear un DataFrame de pandas a partir del diccionario
df = pd.DataFrame.from_dict(registro_pluvial, orient='index').transpose()

# Guardar el DataFrame como archivo CSV
nombre_archivo = 'registro_pluvial_2022.csv'
df.to_csv(nombre_archivo, index=False)

print(f"Archivo CSV generado: {'registro_pluvial_2023.csv'}")

# Crear gráficos
# 1. Gráfico de barras de lluvias anuales
lluvias_anuales = df.sum()
plt.figure(figsize=(10, 5))
lluvias_anuales.plot(kind='bar', color='blue', alpha=0.7)
plt.title('Lluvias Anuales por Mes')
plt.xlabel('Meses')
plt.ylabel('Milímetros de Lluvia')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('lluvias_anuales.png')  # Guardar gráfico
plt.show()

# 2. Gráfico de dispersión
dias = np.arange(1, 32)  # Días del mes
for mes in range(len(meses)):
    plt.scatter([mes + 1] * len(df[meses[mes]]), df[meses[mes]], label=meses[mes])

plt.title('Lluvias Diarias por Mes')
plt.xlabel('Meses')
plt.ylabel('Milímetros de Lluvia')
plt.xticks(ticks=np.arange(1, 13), labels=meses, rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('lluvias_diarias_por_mes.png')  # Guardar gráfico
plt.show()

# 3. Gráfico circular
lluvias_totales = df.sum(axis=0)
plt.figure(figsize=(8, 8))
plt.pie(lluvias_totales, labels=meses, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de Lluvias por Mes')
plt.axis('equal')  # Igualar proporciones
plt.tight_layout()
plt.savefig('distribucion_lluvias_mensual.png')  # Guardar gráfico
plt.show()