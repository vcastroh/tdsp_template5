# Definición de los datos

## Origen de los datos

- La fuente de datos se obtuvo de Kaggle, de un conjunto relacionado con la incidencia de accidentes cerebrovasculares.

## Especificación de los scripts para la carga de datos

- Los scripts utilizados para la carga de datos se encuentran en el archivo "load_data.py".

## Referencias a rutas o bases de datos origen y destino

### Rutas de origen de datos

- Estructura de los archivos de origen de los datos: CSV con columnas separadas por comas.

- Procedimientos de transformación y limpieza de los datos:
  - Se eliminó la columna 'id' ya que no tiene relación con la probabilidad de sufrir un accidente cerebrovascular.


### Base de datos de destino

- Base de datos de destino para los datos: `AccidenteCerebrovascularDB`.
- Estructura de la base de datos de destino: Conjunto de tablas relacionales.
