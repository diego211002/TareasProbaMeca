# Programa para Tarea 1: Estadistica Descriptiva
# Analisis estadistico de datos de Concentración real de benceno promediada
# por hora en microg/m^3 por sensor C6H6 (GT)

# Librerias Utilizadas

###################################################
import pandas as pd
from statistics import multimode, StatisticsError
import numpy as np
import math
import matplotlib.pyplot as plt
###################################################


# Funciones para analisis estadistico

# Leer  archivo CSV
C6H6GT_data = pd.read_csv("AirQualityUCI.csv", delimiter=';')


#  Extrae la columna C6H6(GT) del archivo
datos = C6H6GT_data['C6H6(GT)']

#  reemplaza las comas de los datos por puntos
strDatos = datos.str.replace(',', '.')

# convierte los datos a tipo float y
# elimina las filas que no tengan un valor numérico
float_datos = strDatos.astype(float).dropna()

# obtiene los datos que son mayores a cero
float_datos_filtrados = float_datos[float_datos > 0]

n = len(float_datos_filtrados)  # cantidad de datos de la columna


#  Funcion para calcular promedio de datos
def promedio_de_datos():
    promedio = sum(float_datos_filtrados)/n  # Calcula el promedio
    # promedio = datos.mean()
    return (promedio)


promedio = promedio_de_datos()

print("Promedio: ", promedio, "microg/m^3")


# Funcion para calcular el rango de la muestra con minimo y maximo
def rango_de_datos(C6H6GT_data):
    minimo = min(float_datos_filtrados)
    maximo = max(float_datos_filtrados)
    rango_muestral = maximo-minimo  # Formula de rango
    print("Rango: ", rango_muestral, "microg/m^3")


rango_de_datos(C6H6GT_data)


def moda_de_datos(C6H6GT_data):
    # Verifica que haya datos suficientes después de filtrar
    if len(float_datos_filtrados) == 0:
        print("No hay datos no negativos en la muestra.")
        return None

    try:
        # Verifica si hay más de una moda usando multimode
        modas = multimode(float_datos_filtrados)
        if len(modas) == 1:
            print("Moda: ", modas[0], "microg/m^3")
        else:
            print("Múltiples modas: ", modas, "microg/m^3")
    except StatisticsError:
        print("No se puede encontrar una moda única o los datos están vacíos.")


moda_de_datos(C6H6GT_data)


# Función para calcular la mediana de la muestra de datos
def mediana_de_datos(C6H6GT_data):
    # Libreria numpy para encontrar mediana
    mediana = np.median(float_datos_filtrados)
    print("Mediana: ", mediana, "microg/m^3")


# Función para calcular los cuartiles y el rango intercuartilico (RIC)
# Función para calcular los cuartiles y el rango intercuartilico (RIC)
def cuartiles_de_datos(C6H6GT_data):
    # Libreria numpy para encontrar Q1
    Q1 = np.percentile(float_datos_filtrados, 25)
    # Este es igual a la mediana
    Q2 = np.percentile(float_datos_filtrados, 50)
    # Libreria numpy para encontrar Q3
    Q3 = np.percentile(float_datos_filtrados, 75)
    RIC = Q3 - Q1  # Formula de rango intercuartilico
    print("Q1 :", Q1, "microg/m^3")
    print("Q2 :", Q2, "microg/m^3")
    print("Q3 :", Q3, "microg/m^3")
    print("RIC :", RIC, "microg/m^3")
    return Q1, Q2, Q3, RIC


cuartiles_de_datos(C6H6GT_data)


#  Funcion que calcula la varianza de los datos
def varianza_datos():
    # Libreria Pandas para encontrar la varianza
    s_2 = float_datos_filtrados.var()
    return s_2


varianza = varianza_datos()
print("Varianza :", varianza)


#  Funcion que calcula la desviacion estandar de los datos
def desviacion_estandar_datos():
    s = math.sqrt(varianza)  # Calcula la raiz cuadrada de la varianza
    return s


desviacion_estandar = desviacion_estandar_datos()
print("Desviacion estandar :", desviacion_estandar)


#  Funcion que calcula el coeficiente de variacion de datos
def coeficiente_variacion_datos():
    c_v = desviacion_estandar/promedio  # Formula para C.V
    return c_v


coeficiente_variacion = coeficiente_variacion_datos()
print("C.V: ", coeficiente_variacion)


# Diagrama de Cajas #

cuar1, cuar2, cuar3, rango_intercuartil = cuartiles_de_datos(C6H6GT_data)


# Calcula limite inferior y superior de los bigotes
# del diagrama de cajas (distancia)
lim_inferior = cuar1 - 1.5 * rango_intercuartil
lim_superior = cuar3 + 1.5 * rango_intercuartil


# Identifica valores atípicos basados en los limites
def encontrar_valores_atipicos():
    valores_atipicos = []

    for i in float_datos_filtrados:
        if i < lim_inferior or i > lim_superior:
            valores_atipicos.append(i)

    return valores_atipicos


valor_atipico = encontrar_valores_atipicos()


# Identifica valores que se encuentran dentro de los limites
def encontrar_datos_dentro_limites():
    valores_dentro_limites = []
    for i in float_datos_filtrados:
        if lim_inferior <= i <= lim_superior:
            valores_dentro_limites.append(i)
    return valores_dentro_limites


valores_dentro_lim = encontrar_datos_dentro_limites()


min_dentro_lim = min(valores_dentro_lim)
max_dentro_lim = max(valores_dentro_lim)


fig, ax = plt.subplots()  # crea el gráfico y los ejes


# Muestra el titulo y las etiquetas
ax.set_title('Concentración real de benceno promediada por hora en microg/m^3')
ax.set_xlabel('microg/m^3')


# Oculta el eje y de la grafica
ax.get_yaxis().set_visible(False)


# Dibuja la caja desde el cuartil 1 al cuartil 3
ax.add_patch(plt.Rectangle((cuar1, 0.75), rango_intercuartil, 0.5, fill=True, color='aquamarine'))


# Dibuja la linea de la mediana
ax.plot([cuar2, cuar2], [0.75, 1.25], color='deeppink', lw=1)


# Dibuja los bigotes desde el cuartil 1
# hasta el minimo y del cuartil 3 hasta el maximo
ax.plot([min_dentro_lim, cuar1], [1, 1], color='black', lw=1)
ax.plot([cuar3, max_dentro_lim], [1, 1], color='black', lw=1)


# Dibuja las lineas verticales de los extremos de los bigotes
ax.plot([min_dentro_lim, min_dentro_lim], [0.8, 1.2], color='black', lw=1)
ax.plot([max_dentro_lim, max_dentro_lim], [0.8, 1.2], color='black', lw=1)


# Dibuja los datos atipicos como puntos
ax.scatter(valor_atipico, [1]*len(valor_atipico), color='deepskyblue')


plt.show()


# Histograma #

def numero_de_clases(n):
    clases = int(np.ceil(np.sqrt(n)))

    return clases


# Se calcula el número de clases usando diferentes reglas
clases = numero_de_clases(n)


# Se calcula el intervalo de las clases
min_val = min(float_datos_filtrados)
max_val = max(float_datos_filtrados)
intervalo_bin = (max_val - min_val) / clases


# Se crean los intervalos de las clases para histograma
intervalos = np.arange(min_val, max_val + intervalo_bin, intervalo_bin)


# Calculo de frecuencia absoluta
frecuencia_absoluta, _ = np.histogram(float_datos_filtrados, bins=intervalos)


# Calculo la frecuencia relativa
frecuencia_relativa = frecuencia_absoluta / len(float_datos_filtrados)


# Creacion del histograma de frecuencia absoluta respecto a los datos
plt.figure(figsize=(10, 6))
plt.hist(float_datos_filtrados, bins=intervalos, color='skyblue', edgecolor='black')
plt.title('Concentración real de benceno promediada por hora en microg/m^3')
plt.xlabel('microg/m^3')
plt.ylabel('Frecuencia Absoluta')
plt.show()
