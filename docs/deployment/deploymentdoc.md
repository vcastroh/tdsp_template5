# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:**  Random Forest Stroke Prediction Model
- **Plataforma de despliegue:** Railway
- **Requisitos técnicos:** Python 3.7 o superior
                           Bibliotecas: scikit-learn, fastapi, uvicorn

## Código de despliegue

- **Archivo principal:** main.py
- **Rutas de acceso a los archivos:** main.py
                                      model.joblib
                                      requirements.txt
                                      railway.json

## Documentación del despliegue

- **Instrucciones de instalación:**
* 1- Clona el repositorio: git clone https://github.com/vcastroh/tdsp_template5
* 2- Ingresa al directorio del proyecto: cd mlapi
* 3- Instala las dependencias: pip install -r requirements.txt
- **Instrucciones de configuración:** No hay configuraciones específicas necesarias.
- **Instrucciones de uso:** 
* 1- Iniciar la aplicación FastAPI: uvicorn main:app --host 0.0.0.0 --port $PORT
* 2- Acceder a la API en tu navegador o mediante herramientas como curl o Postman.
* 3- Realizar solicitudes POST a la ruta /predict con datos en el cuerpo de la solicitud según la estructura definida en ApiInput.
- **Instrucciones de mantenimiento:** Para actualizar el modelo, simplemente reemplaza el archivo model.joblib con la versión actualizada del modelo.
