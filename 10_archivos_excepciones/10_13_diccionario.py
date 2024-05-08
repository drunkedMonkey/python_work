from pathlib import Path
import json

nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")

diccionario = {"nombre": nombre, "apellido": apellido}

try:
    path = Path("10_archivos_excepciones/diccionario.txt")
    contents = json.dumps(diccionario)
    path.write_text(contents)
except:
    print("Error al escribir el archivo")

try:
    path = Path("10_archivos_excepciones/diccionario.txt")
    contents = path.read_text()
    diccionario = json.loads(contents)
    print(diccionario)
except:
    print("Error al leer el archivo")
