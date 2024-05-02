from pathlib import Path
response = input("Indica Tu nombre para la lista de invitados: ")

path = Path('./10_archivos_excepciones/invitado.txt')
path.write_text(response + '\n')
