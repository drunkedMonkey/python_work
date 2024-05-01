pedidos_bocadillos = ['pollo','pastrami', 'serranito','pastrami','bacon','pastrami', 'atun', 'vegetal']
bocadillos_terminados = []


print("La bocateria ha agotado el pastrami")
while 'pastrami' in pedidos_bocadillos:
    pedidos_bocadillos.remove('pastrami')

while pedidos_bocadillos:
    bocadillo = pedidos_bocadillos.pop()
    print(f"Preparando bocadillo de {bocadillo}")
    bocadillos_terminados.append(bocadillo)

print("\nLos bocadillos preparados son: ")
for bocadillo in bocadillos_terminados:
    print(bocadillo)