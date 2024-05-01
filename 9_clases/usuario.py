class Usuario:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_nombre(self):
        print(f"El nombre del usuario es {self.nombre}")

    def mostrar_apellido(self):
        print(f"El apellido del usuario es {self.apellido}")

    def mostrar_edad(self):
        print(f"La edad del usuario es {self.edad}")

    def describir_usuario(self):
        print(f"El usuario se llama {self.nombre} {self.apellido} y tiene {self.edad} años")