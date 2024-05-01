from usuario import Usuario

class Privilegios:
    def __init__(self):
        self.privilegios = ['puede agregar post', 'puede borrar post', 'puede banear usuarios']
    
    def show_privileges(self):
        print("Privilegios del administrador:")
        for privilege in self.privilegios:
            print(f"- {privilege}")

class Admin(Usuario):
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido, edad)
        self.privilegios = Privilegios()
    
    def mostrar_privilegios(self):
        print("Privilegios del administrador:")
        for privilegio in self.privilegios:
            print(f"- {privilegio}")