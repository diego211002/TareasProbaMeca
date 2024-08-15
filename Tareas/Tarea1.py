import pandas as pd
from statistics import mode
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns

# Leer un archivo CSV
C6H6GT_data = pd.read_csv("AirQualityUCI.csv", delimiter=';')

n = 9357  # cantidad de datos de la columna correspondiente del archivo

#  Extrae la columna C6H6(GT) del archivo
datos = C6H6GT_data['C6H6(GT)']

#  reemplaza las comas de los datos por puntos
strDatos = datos.str.replace(',', '.')

# convierte los datos a tipo float y
# elimina las filas que no tengan un valor numérico
float_datos = strDatos.astype(float).dropna()

# Funcion para realizar promedio de datos


#  Funcion para calcular promedio de datos
def promedio_de_datos():
    promedio = sum(float_datos)/n  # Calcula el promedio
    # promedio = datos.mean()
    return (promedio)


promedio = promedio_de_datos()

print("Promedio: ", promedio)


def rango_de_datos(C6H6GT_data):
    minimo = min(float_datos)
    maximo = max(float_datos)
    rango_muestral = maximo-minimo
    print("Rango: ", rango_muestral)


rango_de_datos(C6H6GT_data)


def moda_de_datos(C6H6GT_data):
    moda = mode(float_datos)
    print("Moda: ", moda)

moda_de_datos(C6H6GT_data)


# Función para calcular la mediana de los datos
def mediana_de_datos(C6H6GT_data):
    mediana = np.median(float_datos)
    print("Mediana: ", mediana)


# mediana_de_datos(C6H6GT_data)


# Función para calcular los cuartiles y el rango intercuartílico (IQR)
def cuartiles_e_iqr(C6H6GT_data):
    Q1 = np.percentile(float_datos, 25)
    Q2 = np.percentile(float_datos, 50)  # Este es igual a la mediana
    Q3 = np.percentile(float_datos, 75)
    IQR = Q3 - Q1
    print("Primer cuartil :", Q1)
    print("Mediana :", Q2)
    print("Tercer cuartil :", Q3)
    print("Rango Intercuartílico :", IQR)


cuartiles_e_iqr(C6H6GT_data)


#  Funcion que calcula la varianza de los datos
def varianza_datos():
    s_2 = sum((float_datos - promedio)**2)/n-1
    return s_2


varianza = varianza_datos()


def desviacion_estandar_datos():
    s = math.sqrt(varianza)  # Calcula la raiz cuadrada de la varianza
    return s


desviacion_estandar = desviacion_estandar_datos()


def coeficiente_variacion_datos():
    c_v = desviacion_estandar/promedio
    return c_v


coeficiente_variacion = coeficiente_variacion_datos()
print("C.V: ", coeficiente_variacion)


# ----------- Diagrama de Cajas (Box Plot) Horizontal -----------
# Convertir la serie de datos a una lista para trabajar con Seaborn
float_datos_list = float_datos.tolist()

# Crear el diagrama de cajas (box plot) horizontal usando Seaborn
sns.boxplot(data=float_datos_list, orient='h')  # 'h' para horizontal

# Añadir título y etiquetas
plt.title("Diagrama de Cajas Horizontal de los Datos de C6H6(GT)")
plt.xlabel("Concentración de C6H6(GT)")

# Mostrar el gráfico
plt.show()
