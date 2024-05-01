from pathlib import Path

path = Path('./10_archivos_excepciones/sobrepython.txt')
contents = path.read_text().rstrip()

print(contents)

lines = contents.splitlines()
for line in lines:
    print(line)