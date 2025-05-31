# src/download_data.py

import requests
import os

# ID extraído de tu enlace de Google Drive:
FILE_ID = "1SdKIbIm3SrLa9XtQxlCZXHklp3w8FGEi"
# URL de descarga directa
URL = f"https://drive.google.com/uc?export=download&id={FILE_ID}"

# Ruta local donde se guardará el CSV
LOCAL_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "crimes.csv")

def descargar_csv():
    """
    Descarga el archivo CSV desde Google Drive si aún no existe localmente.
    """
    # Si ya existe, no vuelve a descargar
    if os.path.exists(LOCAL_PATH):
        print(f"El archivo ya existe en: {LOCAL_PATH}")
        return

    # Asegura que la carpeta 'data/' exista
    os.makedirs(os.path.dirname(LOCAL_PATH), exist_ok=True)

    # Petición en streaming para no saturar memoria
    response = requests.get(URL, stream=True)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"Error al intentar descargar el archivo: {e}")
        return

    # Escribe en bloques de 8 KB
    with open(LOCAL_PATH, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print(f"Descarga completada: {LOCAL_PATH}")

if __name__ == "__main__":
    descargar_csv()

