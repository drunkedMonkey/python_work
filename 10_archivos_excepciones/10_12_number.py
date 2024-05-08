from pathlib import Path
import json


path = Path("10_archivos_excepciones/numero_full.json")

if path.exists():
    try:
        contents = json.loads(path.read_text(encoding='utf-8'))
        
    except FileNotFoundError:
        print("No se ha encontrado el archivo")
        pass
    else:
        print(f"Tu número favorito es {contents}")
else:
    try:
        numero = input("Introduce número favorito: ")
        numero = int(numero)
        
        contents = json.dumps(numero)
        
    except ValueError:
        print("No has introducido un número entero.")
    else:
        path.write_text(contents)

    

