# Informe de salida

## Resumen Ejecutivo

A lo largo del proyecto se identificaron desafíos y oportunidades clave y se logró tener un modelo con una robustez aceptable en la detección de la probabilidad de que un individuo sufra un accidente cerebrovascular. El modelo final, basado en el RandomForestClassifier, se destaca por tener una mejor capacidad para identificar casos positivos, a pesar del desequilibrio de clases que presentaban los datos.

## Resultados del proyecto

Inicialmente se realizó la limpieza de los datos, y luego se implementaron y evaluaron múltiples modelos, incluyendo Redes Neuronales Artificiales (ANN), Bosque Aleatorio y Regresión Logística.
La técnica de sobremuestreo SMOTE se aplicó para abordar el desequilibrio de clases, mejorando la capacidad del modelo de ANN.
Finalmente se evidenció que el modelo RandomForestClassifier presentaba un rendimiento superior en la identificación de casos positivos, superando al modelo base y otros modelos evaluados y por ende se seleccionó como el modelo final.
Es importaante resaltar que a pesar de las mejoras con datos sobremuestreados, persisten desafíos en la identificación precisa de casos positivos en el conjunto de datos original.

## Lecciones aprendidas

La calidad de los datos es fundamental, asi como la limpieza y la comprensión de los mismos.

- Recomendaciones para Futuros Proyectos de Machine Learning:
    - Considerar estrategias adicionales para abordar el desequilibrio de clases.

## Impacto del proyecto

El modelo tiene el potencial de mejorar la atención médica preventiva al identificar individuos con mayor riesgo de accidentes cerebrovasculares.

- Áreas de Mejora y Oportunidades de Desarrollo Futuras:
      - Explorar la incorporación de más datos clínicos y biomédicos para mejorar la precisión del modelo.
      - Colaborar con profesionales de la salud para una implementación más efectiva en el área médica.

## Conclusiones

- El proyecto logró desarrollar un modelo de machine learning efectivo para la predicción de accidentes cerebrovasculares.
- El RandomForestClassifier se destacó por su capacidad superior en la identificación de casos positivos, en comparación con los modelos entrenados.
- Se recomienda una exploración continua de técnicas y enfoques para mejorar la precisión del modelo en contextos clínicos y éticos.
- Es importante la colaboración interdisciplinaria para abordar este tipo desafíos. Esto con el fin de lograr modelos más robustos que se puedan utilizar en el área medica.
