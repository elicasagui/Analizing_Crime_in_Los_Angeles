# src/download_data.py

import requests
import os

# Identificador del archivo en Google Drive
FILE_ID = "1SdKIbIm3SrLa9XtQxlCZXHklp3w8FGEi"
# URL para descarga directa a partir del ID
URL = f"https://drive.google.com/uc?export=download&id={FILE_ID}"

# Ruta local donde se guardará el CSV
LOCAL_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "mi_archivo_grande.csv")

def descargar_csv():
    """
    Descarga el archivo CSV desde Google Drive si aún no existe localmente.
    """
    if os.path.exists(LOCAL_PATH):
        print(f"El archivo ya existe en: {LOCAL_PATH}")
        return

    # Crear carpeta de destino si no existe
    os.makedirs(os.path.dirname(LOCAL_PATH), exist_ok=True)

    # Iniciar la solicitud de descarga en modo streaming
    response = requests.get(URL, stream=True)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"Error al intentar descargar el archivo: {e}")
        return

    # Guardar el contenido en bloques para no saturar la memoria
    with open(LOCAL_PATH, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print(f"Descarga completada exitosamente: {LOCAL_PATH}")

if __name__ == "__main__":
    descargar_csv()
