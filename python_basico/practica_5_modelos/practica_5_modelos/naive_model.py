import pickle
import pandas as pd

class NaiveModel:

    """
    Modelo muy simple que calcula la media de cada columna 
    y luego normaliza dividiendo cada valor entre su media.
    """
    def __init__(self):
        """Inicializa el diccionario donde guardaremos las medias."""
        self.means = {}

    def fit(self, df: pd.DataFrame):
        """
        Calcula la media de cada columna del DataFrame y la guarda en self.means.
        """
        if not isinstance(df, pd.DataFrame):
            raise ValueError("El método fit requiere un DataFrame de pandas.")
        
        self.means = df.mean().to_dict()

    def predict(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Devuelve un DataFrame normalizado: valor / media de su columna.
        Se hace una copia profunda para no modificar los datos originales.
        """
        if not self.means:
            raise ValueError("El modelo no ha sido entrenado. Usa fit() antes de predict().")

        df_copy = df.copy(deep=True)

        for col in df_copy.columns:
            if col in self.means and self.means[col] != 0:
                df_copy[col] = df_copy[col] / self.means[col]

        return df_copy

    def save(self, filename: str):
        """
        Guarda en disco las medias mediante pickle.
        """
        with open(filename, "wb") as f:
            pickle.dump(self.means, f)

    def load(self, filename: str):
        """
        Carga desde disco las medias previamente guardadas.
        """
        with open(filename, "rb") as f:
            self.means = pickle.load(f)
            
            
