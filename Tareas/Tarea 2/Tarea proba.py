from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import nbinom
import math

#Parte 1

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
plt.bar(Probabilidad_caso1.keys(), Probabilidad_caso1.values(), width=0.6, color='skyblue', edgecolor='black')
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
plt.bar(Sumas_posibles_Caso2.keys(), Sumas_posibles_Caso2.values(), width=0.6, color='lightcoral', edgecolor='black' )
plt.xlabel('Suma de los Dados')
plt.ylabel('Probabilidad')
plt.title('Distribución de la Suma de Dos Dados de Truco')
plt.show()

# Tabla para la funcion de masa de probabilidad para los dados de truco
df_truco = pd.DataFrame(list(Sumas_posibles_Caso2.items()), columns=['Suma', 'Probabilidad'])
print("\nFunción de Masa de Probabilidad de Dados de Truco")
print(df_truco)



def combinatoria(n, k):
    """Calcula la combinatoria C(n, k) = n! / (k! * (n - k)!)"""
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def binomial_negativa(k, r, p):
    """Calcula la probabilidad para la distribución binomial negativa."""
    coef = combinatoria(k - 1, r - 1)
    prob = coef * (p ** r) * ((1 - p) ** (k - r))
    return prob

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
