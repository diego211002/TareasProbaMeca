from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import binom
from scipy.stats import norm

# Parte 1: Dados Ideales
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


# Parte 2: Dados de Truco
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


# Parte 3

# Distribucion Binomial para VAD

# Parámetros para la distribución binomial
n = 1000
k = 499

# Cálculo de la probabilidad utilizando la distribución binomial para VAD
prob_binom = binom.cdf(k, n, Probabilidad_7_ideal)
print(f"Probabilidad de obtener menos de 500 sietes en 1000 tiradas con Distribucion Binomial es: {prob_binom:.4f}")

# Aproximacion de Distribucion Normal para VAC

# Cálculo de la media y la desviación estándar para la aproximación normal
mu = n * Probabilidad_7_ideal
sigma = (n * Probabilidad_7_ideal * (1 - Probabilidad_7_ideal)) ** 0.5

# Corrección de continuidad
k_normal = 499 + 0.5

# Cálculo de la probabilidad utilizando la aproximación normal
prob_norm = norm.cdf(k_normal, mu, sigma)
print(f"Probabilidad de obtener menos de 500 sietes en 1000 tiradas con Distribucion Normal es: {prob_norm:.4f}")

# Cálculo del error entre ambas aproximaciones
error = abs(prob_binom - prob_norm)
print(f"Error entre la aproximación binomial y normal: {error:.6f}")
