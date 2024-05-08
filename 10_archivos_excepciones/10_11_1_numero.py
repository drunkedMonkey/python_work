from pathlib import Path
import json

numero = input("Introduce número favorito: ")

try:
    numero = int(numero)
    path = Path("10_archivos_excepciones/numero.json")
    contents = json.dumps(numero)
    
except ValueError:
    print("No has introducido un número entero.")
else:
    path.write_text(contents)
