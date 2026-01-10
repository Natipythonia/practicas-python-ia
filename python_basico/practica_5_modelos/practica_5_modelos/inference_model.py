import pandas as pd
from models.naive_model import NaiveModel

# 1. Cargamos el mismo CSV usado en el entrenamiento
url = "https://raw.githubusercontent.com/ivarvb/GFF/refs/heads/master/dataset/MNIST-10000-784.csv"
df = pd.read_csv(url)

# 2. Creamos el modelo y cargamos las medias guardadas
modelo = NaiveModel()
modelo.load("medias_modelo.pkl")

# 3. Aplicamos la inferencia
df_normalizado = modelo.predict(df)

# 4. Guardamos los datos normalizados en un CSV
df_normalizado.to_csv("predicciones.csv", index=False)

print("Inferencia realizada. Archivo generado: predicciones.csv")

