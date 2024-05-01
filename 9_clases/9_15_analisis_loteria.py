from random import choice

lista_posibilidades = [20,15,24,33,14,15,26,37,58,49,'p', 'o','s','a','n']

def generar_numeros():
    count = 0
    numeros_agraciados = []
    while count < 4:
        num = choice(lista_posibilidades)
        if num not in numeros_agraciados:
            numeros_agraciados.append(num)
            count += 1
    return numeros_agraciados

print("#                     #")
print("########Loteria#########")
print("#                     #")

mi_boleto = [20, 49, 33, 'n']

contador_vueltas = 1
premiado = False  # Inicializamos premiado como False
while not premiado:  # Continuará hasta que premiado sea True
    numeros_agraciados = generar_numeros()
    contador_aciertos = 0
    for numero in mi_boleto:
        if numero in numeros_agraciados:
            contador_aciertos += 1
    if contador_aciertos == 4:
        premiado = True  # Actualizamos premiado a True si el boleto es premiado
    else:
        print("Tu boleto no ha sido premiado en la vuelta:", contador_vueltas, 'aciertos:', contador_aciertos, 'Números agraciados:', numeros_agraciados)
        contador_vueltas += 1

print("¡Felicidades! Tu boleto ha sido premiado en la vuelta:", contador_vueltas, 'Números agraciados:', numeros_agraciados)
