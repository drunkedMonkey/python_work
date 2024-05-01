from pathlib import Path

path = Path('./10_archivos_excepciones/sobrepython.txt')
contents = path.read_text().rstrip()

print(contents)

lines = contents.splitlines()
new_lines = []
for line in lines:
    new_line = line.replace('Python', 'C')
    new_lines.append(new_line)

print('\n'.join(new_lines))