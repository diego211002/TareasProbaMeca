from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

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
