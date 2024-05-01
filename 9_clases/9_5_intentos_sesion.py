class Usuario:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.intentos_inicio = 0

    def mostrar_nombre(self):
        print(f"El nombre del usuario es {self.nombre}")

    def mostrar_apellido(self):
        print(f"El apellido del usuario es {self.apellido}")

    def mostrar_edad(self):
        print(f"La edad del usuario es {self.edad}")

    def describir_usuario(self):
        print(f"El usuario se llama {self.nombre} {self.apellido} y tiene {self.edad} años")
    
    def incrementar_intentos_inicio(self):
        self.intentos_inicio += 1

    def restablecer_intentos_inicio(self):
        self.intentos_inicio = 0



yo = Usuario('Pepe', 'Ibanez', 33)

yo.incrementar_intentos_inicio()
yo.incrementar_intentos_inicio()
yo.incrementar_intentos_inicio()
yo.incrementar_intentos_inicio()
print(yo.intentos_inicio)

yo.restablecer_intentos_inicio()
print(yo.intentos_inicio)