# Reporte del Modelo Final

## Resumen Ejecutivo

Este proyecto tiene como objetivo principal desarrollar un modelo de clasificación de aprendizaje automático para predecir la probabilidad de que un individuo sufra un accidente cerebrovascular. Después de una exhaustiva exploración y evaluación de diversos modelos, el RandomForestClassifier demostró un rendimiento robusto en la identificación de casos positivos.

## Descripción del Problema

El problema abordado implica prevenir accidentes cerebrovasculares mediante la identificación temprana de individuos en riesgo. A pesar de los esfuerzos con diversos modelos, el desequilibrio en la distribución de clases presentó desafíos en la identificación precisa de casos positivos.

## Descripción del Modelo

El modelo final es el RandomForestClassifier,ya que mostró una mayor robustez en la identificación de casos positivos. Es importante anotar que se exploraron modelos de ANN, Bosque Aleatorio y Regresión Logística, pero el desequilibrio de clases afectó su rendimiento, aunque la implementación de SMOTE mejoró la capacidad del modelo de ANN, se evidenció que el modelo seguía teniendo limitaciones.

## Evaluación del Modelo

Para evaluar el modelo se tomó en cuenta principalmente el accuracy y el f1-score, el cual mostró un mejor rendimiento en el modelo RandomForestClassifier

## Conclusiones y Recomendaciones

A pesar de los desafíos encontrados, el modelo final ofrece una herramienta valiosa para la identificación temprana de individuos en riesgo de accidentes cerebrovasculares. Es importante mejorar las técnicas de manejo de desequilibrio y ajuste de modelos para mejorar la generalización y robustez del modelo.

## Referencias

Se utilizaron bibliotecas estándar de machine learning como Keras, sklearn, y matplotlib para construir y evaluar el modelo baseline. 
