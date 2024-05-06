from pathlib import Path

def read_files(path):
    try:
        path.read_text()
    except FileNotFoundError:
        print(f"Error: El archivo {path} no existe.")
    else:
        print("Los archivos existen.")


path = Path("gatos.txt")
path_two = Path("10_archivos_excepciones/perros.txt")

read_files(path)
read_files(path_two)


