from pathlib import Path
import json

try:
    path = Path("10_archivos_excepciones/numero.json")
    contents = json.loads(path.read_text(encoding='utf-8'))
    
except FileNotFoundError:
    print("No se ha encontrado el archivo")
    pass
else:
    print(f"Tu número favorito es {contents}")
