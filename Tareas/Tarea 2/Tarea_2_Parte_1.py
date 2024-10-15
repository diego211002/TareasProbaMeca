from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import binom
from scipy.stats import norm

# Parte 1

# Caso 1: Dados Ideales
print(" Dados Ideales ")

# Genera todas las combinaciones posibles de dos dados ideales
Sumas_posibles_Caso1 = [i + j for i in range(1, 7) for j in range(1, 7)]

# Contar frecuencia de cada suma
Distribucion_Caso1 = Counter(Sumas_posibles_Caso1)

# Normaliza para obtener la probabilidad de dados ideales
Combinaciones = sum(Distribucion_Caso1.values())
Probabilidad_caso1 = {k: v / Combinaciones for k, v in Distribucion_Caso1.items()}

# Imprimir resultados de las sumas y sus probabilidades
for sum, prob in Probabilidad_caso1.items():
    print(f"Suma: {sum}, Probabilidad: {prob:.4f}")

# Graficar la distribución para los dados ideales
plt.bar(Probabilidad_caso1.keys(), Probabilidad_caso1.values(), width=0.6)
plt.xlabel('Suma de los Dados Ideales')
plt.ylabel('Probabilidad')
plt.title('Distribución de la Suma de Dos Dados Ideales')
plt.show()

# Tabla para la funcion de masa de probabilidad para los dados ideales
df_ideales = pd.DataFrame(list(Probabilidad_caso1.items()), columns=['Suma', 'Probabilidad'])
print("\nFunción de Masa de Probabilidad de Dados Ideales")
print(df_ideales)


# Caso 2: Dados de Truco
print(" Dados de Truco ")

# Definir las probabilidades para los dados trucados
PrimerDado = [0.06, 0.06, 0.7, 0.06, 0.06, 0.06]  # valor 3 con probabilidad de 0.7
SegundoDado = [0.06, 0.06, 0.06, 0.7, 0.06, 0.06] # valor 4 con probabilidad de 0.7

# Generar todas las combinaciones posibles y calcula sus probabilidades de dados de truco
Sumas_posibles_Caso2 = Counter()
for i, p1 in enumerate(PrimerDado, start=1):
    for j, p2 in enumerate(SegundoDado, start=1):
        Sumas_posibles_Caso2[i + j] += p1 * p2

# Imprime resultados de las sumas y sus probabilidades
for sum, prob in Sumas_posibles_Caso2.items():
    print(f"Suma: {sum}, Probabilidad: {prob:.4f}")

# Graficar la distribución para los dados de truco
plt.bar(Sumas_posibles_Caso2.keys(), Sumas_posibles_Caso2.values(), width=0.6)
plt.xlabel('Suma de los Dados')
plt.ylabel('Probabilidad')
plt.title('Distribución de la Suma de Dos Dados de Truco')
plt.show()

# Tabla para la funcion de masa de probabilidad para los dados de truco
df_truco = pd.DataFrame(list(Sumas_posibles_Caso2.items()), columns=['Suma', 'Probabilidad'])
print("\nFunción de Masa de Probabilidad de Dados de Truco")
print(df_truco)


# Parte 3

# Extraer la probabilidad de obtener la suma 7
Prob_7 = Probabilidad_caso1[7]
print(f"\nProbabilidad de obtener un 7: {Prob_7:.4f}")

# ----- Parámetros -----
n = 1000  # Número de tiradas

# Media y desviación estándar para la distribución normal
mu = n * Prob_7
sigma = (n * Prob_7 * (1 - Prob_7)) ** 0.5

print(f"Media (µ): {mu}, Desviación Estándar (σ): {sigma}")

# ----- Ajuste del rango a 150-180 éxitos -----
k1, k2 = 150, 180  # Rango cercano a la media esperada

# ----- Cálculo de la Probabilidad Binomial -----
prob_binomial = binom.cdf(k2, n, Prob_7) - binom.cdf(k1 - 1, n, Prob_7)
print(f"Probabilidad Binomial para 150 ≤ X ≤ 180: {prob_binomial:.10f}")

# ----- Cálculo de la Probabilidad Normal -----
x1, x2 = k1 - 0.5, k2 + 0.5  # Corrección de continuidad
prob_normal = norm.cdf(x2, mu, sigma) - norm.cdf(x1, mu, sigma)
print(f"Probabilidad Normal para 150 ≤ X ≤ 180: {prob_normal:.10f}")

# ----- Cálculo del Error Relativo -----
if prob_binomial != 0:
    error = abs(prob_binomial - prob_normal) / prob_binomial * 100
    print(f"Error Relativo entre Binomial y Normal: {error:.5f}%")
else:
    print("Error: La probabilidad binomial es cero, no se puede calcular el error.")
