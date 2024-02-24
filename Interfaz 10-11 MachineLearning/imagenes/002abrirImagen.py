from PIL import Image
import os

carpeta = "c:\\xampp\\htdocs\\MachineLearning\\imagenes\\001crudo"

archivos = os.listdir(carpeta)

for archivo in archivos:
    imagen = os.path.join(carpeta,archivo)
    print(imagen)
    miimagen = Image.open(imagen)
    