while True:
    try:
        num_one = float(input("Ingrese el primer número: "))
        num_two = float(input("Ingrese el segundo número: "))
        suma = num_one + num_two
    except ValueError:
        print("Error: Ingrese un número válido.")
    else:
        print(f"La suma de {num_one} y {num_two} es {suma}.")