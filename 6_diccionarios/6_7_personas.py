persona_1 = {'nombre':'Iván', 'apellido': 'Galán', 'edad': 33, 'ciudad': 'Alicante'}
persona_2 = {'nombre':'María', 'apellido': 'López', 'edad': 28, 'ciudad': 'Madrid'}
persona_3 = {'nombre':'Juan', 'apellido': 'García', 'edad': 45, 'ciudad': 'Barcelona'}

personas = [persona_1, persona_2, persona_3]

for persona in personas:
    print(f"Nombre: {persona['nombre']}")
    print(f"Apellido: {persona['apellido']}")
    print(f"Edad: {persona['edad']}")
    print(f"Ciudad: {persona['ciudad']}\n")