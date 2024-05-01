mascota_0={'tipo':'perro','dueño':'juan'}
mascota_1={'tipo':'gato','dueño':'maria'}
mascota_2={'tipo':'pájaro','dueño':'juan'}

mascotas=[mascota_0,mascota_1,mascota_2]

for mascota in mascotas:
    print(f"Tipo: {mascota['tipo']}")
    print(f"Dueño: {mascota['dueño']}\n")