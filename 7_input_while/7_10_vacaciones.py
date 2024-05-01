response = {}

active = True

while active:

    nombre = input("¿Cuál es tu nombre? ")
    destino = input("¿A dónde te gustaría ir de vacaciones? ")
    response[nombre] = destino
    repeat = input("¿Quieres que otra persona responda? (yes/no) ")
    if(repeat == "no"):
        active = False

print("\n--- Resultados de la encuesta ---")
for nombre, destino in response.items():
    print(f"{nombre.title()} le gustaría ir a {destino.title()}.")      

