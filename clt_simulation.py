import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración visual
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 8)
np.random.seed(42)

# ==========================================
# 1. PARÁMETROS DE LA POBLACIÓN (Exponencial)
# ==========================================
scale_parameter = 5.0  # Media de la población (mu = 5)
population_size = 100_000

# Generación de la población altamente sesgada a la derecha
population = np.random.exponential(scale=scale_parameter, size=population_size)
pop_mean = np.mean(population)
pop_std = np.std(population)

print(f"Población original | Media: {pop_mean:.2f} | Desv. Estándar: {pop_std:.2f}")

# ==========================================
# 2. SIMULACIÓN DEL TEOREMA CENTRAL DEL LÍMITE
# ==========================================
sample_sizes = [5, 30, 50, 100]
num_samples = 2000

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
axes = axes.flatten()

# Graficar Población Original
sns.histplot(population, kde=True, ax=axes[0], color="skyblue", bins=50)
axes[0].axvline(pop_mean, color="red", linestyle="--", label=f"Media Poblacional ({pop_mean:.2f})")
axes[0].set_title("1. Población Original (Exponencial - Sesgada)")
axes[0].set_xlabel("Valor")
axes[0].set_ylabel("Frecuencia")
axes[0].legend()

# Graficar Distribuciones Muestrales para distintos n
for idx, n in enumerate(sample_sizes, start=1):
    # Extracción de muestras y cálculo de medias
    sample_means = [np.mean(np.random.choice(population, size=n, replace=True)) for _ in range(num_samples)]
    
    mean_of_means = np.mean(sample_means)
    std_of_means = np.std(sample_means)
    theoretical_std = pop_std / np.sqrt(n)
    
    # Histograma con ajuste normal
    sns.histplot(sample_means, kde=True, ax=axes[idx], color="mediumseagreen", stat="density", bins=30)
    
    axes[idx].axvline(mean_of_means, color="red", linestyle="--", label=f"Media de Medias: {mean_of_means:.2f}")
    axes[idx].set_title(f"n = {n} | EE Real: {std_of_means:.2f} (Teórico: {theoretical_std:.2f})")
    axes[idx].set_xlabel("Valor de la Media")
    axes[idx].set_ylabel("Densidad")
    axes[idx].legend()

# Ocultar el sexto panel sobrante
fig.delaxes(axes[5])
plt.tight_layout()
plt.show()
