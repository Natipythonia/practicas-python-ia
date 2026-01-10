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

### Datos de salida
El archivo `predicciones.csv` **no se incluye en el repositorio** debido a su tamaño.
Este archivo se genera automáticamente al ejecutar el script de inferencia.

### Tecnologías
- Python
- Programación modular
- Serialización de modelos


