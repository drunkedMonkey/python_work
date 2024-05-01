class Privilegios:
    def __init__(self):
        self.privilegios = ['puede agregar post', 'puede borrar post', 'puede banear usuarios']
    
    def show_privileges(self):
        print("Privilegios del administrador:")
        for privilege in self.privilegios:
            print(f"- {privilege}")

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

class Admin(Usuario):
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido, edad)
        self.privilegios = Privilegios()
    
    def mostrar_privilegios(self):
        print("Privilegios del administrador:")
        for privilegio in self.privilegios:
            print(f"- {privilegio}")


admin = Admin('Pepe', 'Ibanez', 33)
admin.privilegios.show_privileges()