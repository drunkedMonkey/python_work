from pathlib import Path

path = Path('./10_archivos_excepciones/sobrepython.txt')
contents = path.read_text().rstrip()

print(contents)

# Eliminamos la variable temporal del ejecicio 10.1 lines y lo hacemos en una sola linea al iterar sobre el contenido

for line in contents.splitlines():
    print(line)