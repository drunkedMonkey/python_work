lista_mensajes = [
    'hola mundo',
    'hola python',
    'hola programadores'
]

mensajes_enviados = []

def enviar_mensajes(mensajes, enviados):
    while mensajes:
        mensaje = mensajes.pop()
        print(mensaje)
        enviados.append(mensaje)

enviar_mensajes(lista_mensajes, mensajes_enviados)

print("\nLos mensajes enviados son: ")
for mensaje in mensajes_enviados:
    print(mensaje)

print("\nLos mensajes restantes son: ")
print(lista_mensajes)