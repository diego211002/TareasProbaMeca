import pandas as pd
from scipy.stats import ttest_1samp, ttest_ind
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
file_path = 'Conjunto_datos_tarea3.xlsx'
# file_path = '/mnt/data/Conjunto_datos_tarea3.xlsx'
df = pd.read_excel(file_path)

# Valor de rendimiento mínimo aceptable (70%)
threshold = 70

results = {}

# Parte 1: Pruebas de hipótesis de una muestra
configurations = ['Inicial', 'Primer_cambio', 'Segundo_cambio']
for config in configurations:
    data = df[config]
    # Realizar la prueba t de una muestra (comparando con el rendimiento mínimo)
    t_stat, p_value = ttest_1samp(data, threshold, alternative='greater')
    results[config] = {'t_statistic': t_stat, 'p_value': p_value}

print("Resultados de la prueba de hipótesis para rendimiento mínimo (70%):")
for config, res in results.items():
    print(f"{config}: Estadístico t = {res['t_statistic']:.4f}, Valor p = {res['p_value']:.4e}")


# Parte 2: Comparaciones entre configuraciones (pruebas de dos muestras independientes)
comparisons = {
    'Inicial vs Primer cambio': ttest_ind(df['Inicial'], df['Primer_cambio']),
    'Inicial vs Segundo cambio': ttest_ind(df['Inicial'], df['Segundo_cambio']),
    'Primer cambio vs Segundo cambio': ttest_ind(df['Primer_cambio'], df['Segundo_cambio'])
}


print("\nResultados de la prueba de hipótesis entre configuraciones:")
for pair, result in comparisons.items():
    print(f"{pair}: Estadístico t = {result.statistic:.4f}, Valor p = {result.pvalue:.4e}")


# Parte 3: Visualización de datos
# Todos los cambios
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[configurations])
plt.axhline(y=threshold, color='r', linestyle='--', label='Rendimiento aceptable (70%)')
plt.title('Distribución del rendimiento para cada configuración')
plt.ylabel('Rendimiento (%)')
plt.xlabel('Configuraciones')
plt.legend()
plt.show()

# Inicial vs Primer cambio
plt.figure(figsize=(8, 5))
sns.boxplot(data=df[['Inicial', 'Primer_cambio']])
plt.axhline(y=threshold, color='r', linestyle='--', label='Rendimiento aceptable (70%)')
plt.title('Comparación del rendimiento: Inicial vs Primer cambio')
plt.ylabel('Rendimiento (%)')
plt.xlabel('Configuraciones')
plt.legend()
plt.show()

# Inicial vs Segundo cambio
plt.figure(figsize=(8, 5))
sns.boxplot(data=df[['Inicial', 'Segundo_cambio']])
plt.axhline(y=threshold, color='r', linestyle='--', label='Rendimiento aceptable (70%)')
plt.title('Comparación del rendimiento: Inicial vs Segundo cambio')
plt.ylabel('Rendimiento (%)')
plt.xlabel('Configuraciones')
plt.legend()
plt.show()

# Primer cambio vs Segundo cambio
plt.figure(figsize=(8, 5))
sns.boxplot(data=df[['Primer_cambio', 'Segundo_cambio']])
plt.axhline(y=threshold, color='r', linestyle='--', label='Rendimiento aceptable (70%)')
plt.title('Comparación del rendimiento: Primer cambio vs Segundo cambio')
plt.ylabel('Rendimiento (%)')
plt.xlabel('Configuraciones')
plt.legend()
plt.show()


# Parte 4: Inferencia estadística
def inferencia_estadistica(results, comparisons):
    print("\nInferencia estadística:")
    # Evaluar aceptabilidad de configuraciones
    for config, res in results.items():
        if res['p_value'] < 0.05:
            print(f"La configuración {config} tiene un rendimiento significativamente mayor al límite aceptable del 70%.")
        else:
            print(f"La configuración {config} no tiene un rendimiento significativamente mayor al límite aceptable del 70%.")

    # Comparar la primera mejora
    if comparisons['Inicial vs Primer cambio'].pvalue < 0.05:
        print("La primera mejora (Primer cambio) representa una mejora significativa respecto a la configuración inicial.")
    else:
        print("La primera mejora (Primer cambio) no representa una mejora significativa respecto a la configuración inicial.")

    # Determinar la mejor configuración
    mejor_config = min(comparisons, key=lambda x: comparisons[x].pvalue)
    print(f"La configuración que más beneficia a la empresa es la que presenta la mayor diferencia significativa: {mejor_config}.")


# Llamar a la función de inferencia estadística
inferencia_estadistica(results, comparisons)
