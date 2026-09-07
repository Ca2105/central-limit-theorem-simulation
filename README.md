# 📊 Central Limit Theorem (CLT) Simulation in Python

Demostración práctica del **Teorema Central del Límite (TCL)** utilizando simulaciones de Monte Carlo con Python (`NumPy`, `Matplotlib` y `Seaborn`). 

El objetivo de este proyecto es validar empíricamente cómo la distribución de las medias muestrales de una población altamente asimétrica converge hacia una distribución normal estándar a medida que incrementa el tamaño de la muestra ($n$).

## 🎯 Objetivos del Proyecto
1. Generar una población no normal (Distribución Exponencial con $\mu = 5.0$).
2. Evaluar el comportamiento de las medias muestrales para tamaños de muestra $n \in \{5, 30, 50, 100\}$.
3. Comprobar la reducción del Error Estándar ($\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$).
4. Conectar el fundamento estadístico con la toma de decisiones en analítica de negocio (A/B Testing e Intervalos de Confianza).

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.10+
* **Librerías:** `numpy`, `matplotlib`, `seaborn`

## 📈 Resultados Visuales
A pesar de que la población origen presenta un sesgo extremo a la derecha, a partir de $n \ge 30$ la distribución de las medias adopta una simetría campaniforme (Normal), demostrando la solidez del TCL en datos del mundo real.
