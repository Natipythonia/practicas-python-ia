import pandas as pd
from models.naive_model import NaiveModel

# 1. Leemos el CSV desde internet
url = "https://raw.githubusercontent.com/ivarvb/GFF/refs/heads/master/dataset/MNIST-10000-784.csv"
df = pd.read_csv(url)

# 2. Creamos el modelo
modelo = NaiveModel()

# 3. Entrenamos el modelo (calculamos las medias)
modelo.fit(df)

# 4. Guardamos las medias en un archivo pickle
modelo.save("medias_modelo.pkl")

print("Modelo entrenado y medias guardadas en: medias_modelo.pkl")

