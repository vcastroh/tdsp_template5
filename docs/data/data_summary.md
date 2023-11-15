# Reporte de Datos

## Resumen general de los datos

El conjunto de datos inicial consta de 5110 observaciones y 12 variables. Las variables incluyen información demográfica, historial médico y otros indicadores relevantes para la predicción de accidentes cerebrovasculares. 
No se observaron valores faltantes en la mayoría de las variables, con excepción de la variable "bmi," que presenta 201 valores nulos, para solucionar esto se hizó la sustitución de los valores nulos en "bmi" por la media de la columna.


## Resumen de calidad de los datos

- Valores Faltantes: La variable "bmi" presenta 201 valores nulos, que se han sustituido por la media de la columna.
- Valores Extremos: No se identificaron valores extremos en las variables numéricas.
- Errores y Duplicados: No se detectaron errores ni duplicados en el conjunto de datos.

## Variable objetivo

La variable objetivo es "stroke," que indica la presencia de un accidente cerebrovascular. El conjunto de datos está desbalanceado, ya que la mayoría de las observaciones corresponden a individuos que no han sufrido un accidente cerebrovascular (stroke=0). Por lo tanto se usó la técnica SMOTE para balancear los datos.

## Variables individuales

- Gender
   - Descripción: La mayoría de las observaciones son de género femenino.
   - Gráfico: Se presenta un gráfico de la distribución de género.
- Age
   - Descripción: La edad de los pacientes varía en el conjunto de datos.
   - Estadísticas Descriptivas: Se incluyen estadísticas descriptivas como media, mediana, y desviación estándar.
- Hypertension y heart_disease
   - Descripción: La mayoría de los pacientes no tienen hipertensión ni enfermedad cardíaca.
   - Gráficos: Se presentan gráficos de distribución para ambas variables binarias.
- Ever_married y work_type
   - Descripción: La mayoría de los pacientes están casados y trabajan en el sector privado.
   - Gráficos: Se incluyen gráficos de distribución para ambas variables categóricas.
- Residence_type
   - Descripción: La distribución de tipos de residencia es equilibrada.
   - Gráfico: Se presenta un gráfico de distribución para la variable categórica "Residence_type."
- avg_glucose_level y bmi
   - Descripción: Se incluyen estadísticas descriptivas para ambas variables numéricas.
- smoking_status
   - Descripción: La mayoría de los pacientes tienen un estado de fumador desconocido.
   - Gráfico: Se presenta un gráfico de distribución para la variable categórica "smoking_status."


## Relación entre variables explicativas y variable objetivo

Se exploraró la relación entre las variables explicativas y la variable objetivo utilizando la matriz de correlación