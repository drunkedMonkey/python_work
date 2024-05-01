personas = input("¿Cuántas personas sois? ")

personas = int(personas)

if personas > 8:
    print("Lo siento, no hay mesas disponibles, tienen que esperar.")
else:
    print("Hay mesa disponible.")