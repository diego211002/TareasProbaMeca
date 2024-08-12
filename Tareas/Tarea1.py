import pandas as pd


usecols = ['C6H6(GT)']

# Leer un archivo CSV
# Realiza operaciones con los datos
C6H6GT_data = pd.read_csv("AirQualityUCI.csv", usecols=["C6H6(GT)"], delimiter=';')

# Imprime los resultados

# print(C6H6GT_data)

n = 9357

# Funcion para realizar promedio de datos

def promedio_de_datos(C6H6GT_data, n):
    datos = C6H6GT_data['C6H6(GT)'].str.replace(',', '.').astype(float).dropna()
    # Datos de excel en punto flotante reemplazando . por ,
    # promedio = sum(datos)/n
    promedio = datos.mean()
    print(promedio)


promedio_de_datos(C6H6GT_data, n)
