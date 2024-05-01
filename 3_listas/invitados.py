invitados = ['Papá', 'Mamá', 'Hermano', 'Hermana', 'Abuelo', 'Abuela']

message = "te invito a cenar"

print(f"{invitados[0]} {message}")
print(f"{invitados[1]} {message}")
print(f"{invitados[2]} {message}")
print(f"{invitados[3]} {message}")
print(f"{invitados[4]} {message}")
print(f"{invitados[5]} {message}")

no_asiste = 'Abuelo'


invitados.insert(4,'Iván')
invitados.remove(no_asiste)

print(f"{invitados[0]} {message}")
print(f"{invitados[1]} {message}")
print(f"{invitados[2]} {message}")
print(f"{invitados[3]} {message}")
print(f"{invitados[4]} {message}")
print(f"{invitados[5]} {message}")

print("He encontrado una mesa más grande, así que puedo invitar a más personas")

invitados.insert(0, 'Juan')
invitados.insert(3, 'Lucas')
invitados.append('Blanca')
                 
print(f"{invitados[0]} {message}")
print(f"{invitados[1]} {message}")
print(f"{invitados[2]} {message}")
print(f"{invitados[3]} {message}")
print(f"{invitados[4]} {message}")
print(f"{invitados[5]} {message}")
print(f"{invitados[6]} {message}")
print(f"{invitados[7]} {message}")
print(f"{invitados[8]} {message}")

print("Lo siento, solo puedo invitar a dos personas")

print(f"{invitados.pop()} lo siento, no puedo invitarte a cenar")
print(f"{invitados.pop()} lo siento, no puedo invitarte a cenar")
print(f"{invitados.pop()} lo siento, no puedo invitarte a cenar")
print(f"{invitados.pop()} lo siento, no puedo invitarte a cenar")
print(f"{invitados.pop()} lo siento, no puedo invitarte a cenar")
print(f"{invitados.pop()} lo siento, no puedo invitarte a cenar")
print(f"{invitados.pop()} lo siento, no puedo invitarte a cenar")

print(f"{invitados[0]} {message}")
print(f"{invitados[1]} {message}")

del invitados[0]
del invitados[0]

print(invitados)
print(len(invitados))





