# Definición de los datos

## Origen de los datos

- La fuente de datos se obtuvo de Kaggle, de un conjunto relacionado con la incidencia de accidentes cerebrovasculares.

## Especificación de los scripts para la carga de datos

- Los scripts utilizados para la carga de datos se encuentran en el archivo "carga_datos.ipynb".

## Referencias a rutas o bases de datos origen y destino

### Rutas de origen de datos

- Estructura de los archivos de origen de los datos: CSV con columnas separadas por comas.

- Procedimientos de transformación y limpieza de los datos:
   - En la fase de preparación de datos primero se identificaron los valores nulos en la columna "bmi," y se remplazaron con la media de la columna. 
   - La columna "age" se transformó a tipo de dato int64.
   - Se realizó un mapeo de los valores en la columna "gender" a números, cambiando su tipo de dato a uint8.
   - Las variables binarias "hypertension" y "heart_disease" se transformaron a tipo de dato uint8. 
   - La variable "smoking_status" se codificó utilizando LabelEncoder y se conviertió a tipo de dato uint8.
   - La columna "ever_married" se codificó a valores binarios (1 para 'Yes' y 0 para 'No'), cambiando su tipo de dato a uint8. Similarmente, "Residence_type" se codificó a valores binarios y se convierte a tipo de dato uint8.
   - Para la variable categórica "work_type," se contaron las ocurrencias de cada categoría y se crearon variables dummy y finalmente las columnas originales se eliminaron.
   - Se revisaron la forma y los tipos de datos después de todas las transformaciones y se creó un mapa de correlación para evaluar las relaciones entre las variables.
   - Finalmente, se realizó la división del conjunto de datos en conjuntos de entrenamiento y validación, y se aplicó la normalización de los datos utilizando MinMaxScaler.
