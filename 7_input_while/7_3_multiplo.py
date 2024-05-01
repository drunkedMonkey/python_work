numero = input("Introduce un número y te diré si es múltiplo de 10: ")
numero = int(numero)

if numero % 10 == 0:
    print(f"El número {numero} es múltiplo de 10.")
else:
    print(f"El número {numero} no es múltiplo de 10.")