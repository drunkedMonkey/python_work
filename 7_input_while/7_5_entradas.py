while True:
    edad = input("Introduce tu edad: ")
    if(edad == "quit"):
        break
    edad = int(edad)
    if(edad < 3):
        print("La entrada es gratuita.")
    elif(edad >= 3 and edad <= 12):
        print("La entrada cuesta 8€.")
    else:
        print("La entrada cuesta 12€.")