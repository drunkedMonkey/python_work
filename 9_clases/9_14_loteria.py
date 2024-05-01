from random import choice

lista_posibilidades = [20,15,24,33,14,15,26,37,58,49,'p', 'o','s','a','n']
print("#                     #")
print("########Loteria#########")
print("#                     #")

count = 0
numeros_agraciados = []
while count < 4:
    num = choice(lista_posibilidades)
    if num not in numeros_agraciados:
        numeros_agraciados.append(num)
        count += 1

print("Numeros o letras agraciad@s: ")

for numero in numeros_agraciados:
    print(numero)


