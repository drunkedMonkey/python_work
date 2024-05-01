ingredientes = []
active = True

while active: 

    ingrediente = input("¿Qué ingredientes quieres en tu pizza? ")
    if(ingrediente == "quit"):
        active = False
    else:
        ingredientes.append(ingrediente)

print("Los ingredientes de tu pizza son: ")
for ingrediente in ingredientes:
    print(ingrediente)