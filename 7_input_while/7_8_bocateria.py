pedidos_bocadillos = ['pollo', 'serranito', 'bacon', 'atun', 'vegetal']
bocadillos_terminados = []

while pedidos_bocadillos:
    bocadillo = pedidos_bocadillos.pop()
    print(f"Preparando bocadillo de {bocadillo}")
    bocadillos_terminados.append(bocadillo)

print("\nLos bocadillos preparados son: ")
for bocadillo in bocadillos_terminados:
    print(bocadillo)