# Reporte del Modelo Baseline

Este informe detalla los resultados obtenidos del modelo baseline, el cual fue el primer modelo construido y se utilizó como punto de referencia para evaluar el rendimiento de modelos subsiguientes.

## Descripción del modelo

El modelo baseline implementado es una Red Neuronal Artificial (ANN) con la siguiente arquitectura:
Modelo:
- Capa de entrada: 14 nodos (variables de entrada)
- Capa oculta 1: 32 nodos, activación ReLU
- Capa oculta 2: 128 nodos, activación ReLU
- Capa oculta 3: 8 nodos, activación ReLU
- Capa de salida: 1 nodo, activación sigmoide

## Variables de entrada

La lista de variables de entrada utilizadas en el modelo se compone de 14 características específicas.

## Variable objetivo

La variable objetivo es 'smoking_status', la cual es binaria y se enfoca en la clasificación.

## Evaluación del modelo

### Métricas de evaluación

El modelo fue evaluado utilizando métricas estándar para problemas de clasificación binaria, incluyendo binary crossentropy como función de pérdida y binary accuracy.

### Resultados de evaluación

Los resultados del modelo baseline después de 20 epochs de entrenamiento son los siguientes:

- Pérdida: 0.1460
- Precisión binaria: 95.46%

## Análisis de los resultados

El modelo baseline mostró una alta precisión global del 95.46%. Sin embargo, al profundizar en las métricas de clasificación, se observa un bajo F1-score, indicando dificultades en la identificación de casos positivos.
- Fortalezas y Debilidades:
   - Fortalezas: Alta precisión general.
   - Debilidades: Bajo F1-score, sugiriendo deficiencias en la identificación de casos positivos.

## Conclusiones

A pesar de la alta precisión general del modelo baseline, su rendimiento en la identificación de casos positivos es limitado, como se refleja en el bajo F1-score, lo cual indica la necesidad de mejoras específicas para abordar el desequilibrio en la clasificación.

## Referencias

Se utilizaron bibliotecas estándar de machine learning como Keras, sklearn, y matplotlib para construir y evaluar el modelo baseline. 

Este modelo baseline sirve como punto de partida para el desarrollo y comparación de modelos subsiguientes, y destaca la importancia de abordar los desafíos específicos en la identificación de casos positivos en el conjunto de datos. Las áreas de mejora podrían incluir técnicas de manejo de desequilibrio y ajustes en la arquitectura del modelo para mejorar la sensibilidad en la detección de casos positivos.
