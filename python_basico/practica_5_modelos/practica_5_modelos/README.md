## Práctica 5 – Modelado y uso de módulos en Python

Esta práctica forma parte del Máster en Inteligencia Artificial y Big Data.

### Objetivo
Implementar un flujo completo de entrenamiento e inferencia de un modelo sencillo,
utilizando **módulos propios**, separación de responsabilidades y buenas prácticas
de organización del código.

### Estructura del proyecto

- `train_model.py`  
  Entrenamiento del modelo y generación del artefacto serializado.

- `inference_model.py`  
  Carga del modelo entrenado y generación de predicciones.

- `models/`  
  Contiene los módulos propios del proyecto:
  - `naive_model.py`
  - `__init__.py`

## Datos de salida

El archivo completo de predicciones (`predicciones.csv`) no se incluye en el repositorio debido a su tamaño.

Para facilitar la revisión del proyecto, se incluye el archivo:

- `predicciones_sample2.csv`

Este archivo contiene **una muestra reducida (subset)** de las predicciones generadas por el modelo, manteniendo la misma estructura y formato que el archivo completo.

El archivo completo de predicciones se genera automáticamente al ejecutar el script de inferencia (`inference_model.py`).


### Tecnologías
- Python
- Programación modular
- Serialización de modelos


