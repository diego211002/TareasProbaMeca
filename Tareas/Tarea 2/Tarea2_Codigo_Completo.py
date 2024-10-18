from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import nbinom
import math
from scipy.stats import binom
from scipy.stats import norm

print("Parte 1")

# Caso 1: Dados Ideales
print("Dados Ideales")

# Genera todas las combinaciones posibles de dos dados ideales
Sumas_posibles_Caso1 = [i + j for i in range(1, 7) for j in range(1, 7)]

# Cuenta frecuencia de cada suma
Distribucion_Caso1 = Counter(Sumas_posibles_Caso1)

# Se encuentra el total de combinaciones posibles y la probabilidad del caso de dados ideales
Total_combinaciones = sum(Distribucion_Caso1.values())  # Usamos un nombre diferente
Probabilidad_caso1 = {k: v / Total_combinaciones for k, v in Distribucion_Caso1.items()}

# Imprime los resultados de las probabilidades
for suma, prob in Probabilidad_caso1.items():
    print(f"Suma: {suma}, Probabilidad: {prob:.4f}")

# Grafica para la distribución para los dados ideales
plt.bar(Probabilidad_caso1.keys(), Probabilidad_caso1.values(), width=0.6)
plt.xlabel('Suma de Dados Ideales')
plt.ylabel('Probabilidad')
plt.title('Distribución de la Suma de Dos Dados Ideales')
plt.show()

# Tabla para la función de masa de probabilidad para los dados ideales
Tabla_ideales = pd.DataFrame(list(Probabilidad_caso1.items()), columns=['Suma', 'Probabilidad'])
print("\nFunción de Masa de Probabilidad de Dados Ideales")
print(Tabla_ideales)


# Caso 2: Dados de Truco
print("Dados de Truco")

# Se definen las probabilidades de los dados de truco
PrimerDado = [0.06, 0.06, 0.7, 0.06, 0.06, 0.06]  # valor 3 con probabilidad de 0.7
SegundoDado = [0.06, 0.06, 0.06, 0.7, 0.06, 0.06]  # valor 4 con probabilidad de 0.7

# Genera todas las combinaciones posibles y calcula sus probabilidades de dados de truco
Sumas_posibles_Caso2 = Counter()
for i, p1 in enumerate(PrimerDado, start=1):
    for j, p2 in enumerate(SegundoDado, start=1):
        Sumas_posibles_Caso2[i + j] += p1 * p2

# Imprime los resultados de las probabilidades
for suma, prob in Sumas_posibles_Caso2.items():
    print(f"Suma: {suma}, Probabilidad: {prob:.4f}")

# Grafica para la distribución para los dados de truco
plt.bar(Sumas_posibles_Caso2.keys(), Sumas_posibles_Caso2.values(), width=0.6)
plt.xlabel('Suma de Dados de Truco')
plt.ylabel('Probabilidad')
plt.title('Distribución de la Suma de Dos Dados de Truco')
plt.show()

# Tabla para la función de masa de probabilidad para los dados de truco
Tabla_truco = pd.DataFrame(list(Sumas_posibles_Caso2.items()), columns=['Suma', 'Probabilidad'])
print("\nFunción de Masa de Probabilidad de Dados de Truco")
print(Tabla_truco)


# Cálculo del número esperado y desviación estándar de resultados iguales a 7 (Analisis 2)

# Numero de tiradas de los dados para que de 7
n_tiradas = 10

# Para Dados Ideales
Probabilidad_7_ideal = Probabilidad_caso1[7]
Media_Ideal = n_tiradas * Probabilidad_7_ideal
Desviacion_ideal = (n_tiradas * Probabilidad_7_ideal * (1 - Probabilidad_7_ideal)) ** 0.5

# Para Dados de Truco
Probabilidad_7_truco = Sumas_posibles_Caso2[7]
Media_Truco = n_tiradas * Probabilidad_7_truco
Desviacion_Truco = (n_tiradas * Probabilidad_7_truco * (1 - Probabilidad_7_truco)) ** 0.5

# Mostrar Resultados
print(f"Dados Ideales -> Número Esperado: {Media_Ideal:.2f}, Desviación Estándar: {Desviacion_ideal:.2f}")
print(f"Dados de Truco -> Número Esperado: {Media_Truco:.2f}, Desviación Estándar: {Desviacion_Truco:.2f}")

print("Parte 2")

#Parte 2
#Se elegió la distribución binomial negativa
#Función que calcula la combinatoria que proviene de la fórmula de la distribución binomial negativa
def combinatoria(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

#Función que retorna la fórmula de la distribución binomial negativa
def binomial_negativa(k, r, p):
    resultado_combinatoria = combinatoria(k - 1, r - 1)
    probabilidad = resultado_combinatoria * (p ** r) * ((1 - p) ** (k - r))
    return probabilidad

#Función que calcula probabilidad de obtener 3 sietes en 10 lazamientos
def calcular_probabilidades(r, p, max_lanzamientos):
    lanzamientos = []  # Lista para guardar los lanzamientos
    resultados = []  # Lista para guardar las probabilidades

    # Ciclo que calcular la probabilidad para cada lanzamiento
    for i in range(r, max_lanzamientos + 1):
        resultado_probabilidad = binomial_negativa(i, r, p)
        lanzamientos.append(i)
        resultados.append(resultado_probabilidad )

    return lanzamientos, resultados

# Parámetros
r = 3  # Número de éxitos
max_lanzamientos = 10  # Número máximo de lanzamientos

# Caso 1: Dados Ideales
p_ideal = 6 / 36
x_ideal, fmp_ideal = calcular_probabilidades(r, p_ideal, max_lanzamientos)

# Caso 2: Dados de Truco
p_truco = 0.98
x_truco, fmp_truco = calcular_probabilidades(r, p_truco, max_lanzamientos)

# Graficamos para dados ideales
plt.bar(x_ideal, fmp_ideal, width=0.4, color='skyblue', edgecolor='black', label='Dados Ideales')
plt.xlabel('Número de Lanzamientos')
plt.ylabel('Probabilidad')
plt.title('Distribución Binomial Negativa para Dados Ideales')
plt.legend()
plt.show()

# Graficamos para dados de truco
plt.bar(x_truco, fmp_truco, width=0.4, color='lightcoral', edgecolor='black', label='Dados de Truco')
plt.xlabel('Número de Lanzamientos')
plt.ylabel('Probabilidad')
plt.title('Distribución Binomial Negativa para Dados de Truco')
plt.legend()
plt.show()

def imprimir_resultados(titulo, lanzamientos, resultados):
    print(f"\n{titulo}")
    for i in range(len(lanzamientos)):
        print(f"Lanzamientos: {lanzamientos[i]}, Probabilidad: {resultados[i]:.4f}")

# Dados ideales 
imprimir_resultados("Distribución Binomial Negativa para dados ideales", x_ideal, fmp_ideal)

# Dados de truco
imprimir_resultados("Distribución Binomial Negativa para dados de truco", x_truco, fmp_truco)

# Parámetros
p_ideal = 1 / 6  # Probabilidad de obtener un 7 con dados ideales
r = 3  # Queremos obtener al menos 3 sietes
prob_truco = 0.1201  # Probabilidad de obtener 3 sietes en 3 tiradas con dados de truco

# Se hace un ciclo para encontrar el número de lanzamientos con dados ideales
for n in range(3, 50):  # Probamos diferentes valores de lanzamientos
    prob_ideal = 1 - binom.cdf(r - 1, n, p_ideal)  # Probabilidad acumulada de obtener al menos 3 sietes
    if prob_ideal >= prob_truco:
        print(f"Con {n} lanzamientos con dados ideales, la probabilidad de obtener al menos 3 sietes es {prob_ideal:.4f}")
        break

print("Parte 3")

# Parte 3

# Distribucion Binomial para VAD

# Parámetros para la distribución binomial
n = 1000
k = 499.999999999999

# Cálculo de la probabilidad utilizando la distribución binomial para VAD
prob_binom = binom.cdf(k, n, Probabilidad_7_ideal)
print(f"Probabilidad de obtener menos de 500 sietes en 1000 tiradas con Distribucion Binomial es: {prob_binom:.4f}")

# Aproximacion de Distribucion Normal para VAC

# Cálculo de la media y la desviación estándar para la aproximación normal
mu = n * Probabilidad_7_ideal
sigma = math.sqrt(n * Probabilidad_7_ideal * (1 - Probabilidad_7_ideal)) 


# Cálculo de la probabilidad utilizando la aproximación normal
prob_norm = norm.cdf(k, mu, sigma)
print(f"Probabilidad de obtener menos de 500 sietes en 1000 tiradas con Distribucion Normal es: {prob_norm:.4f}")

# Cálculo del error entre ambas aproximaciones
error = abs(prob_binom - prob_norm)
print(f"Error entre la aproximación binomial y normal: {error:.12f}")