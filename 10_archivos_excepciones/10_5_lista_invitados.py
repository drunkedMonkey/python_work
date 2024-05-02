from pathlib import Path

libro_invitados = ''
response = ''

path = Path('./10_archivos_excepciones/libro_invitados.txt')

while response != 'end':
    response = input("Indica Tu nombre para la lista de invitados (para salir escribe end): ")
    if response != 'end':
        libro_invitados += response + '\n'
    else:
        print('Lista de invitados generada.')

path.write_text(libro_invitados)