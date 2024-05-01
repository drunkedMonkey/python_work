class Restaurante:
    def __init__(self, nombre, tipo):
        self.nombre_restaurante = nombre
        self.tipo_cocina = tipo

    def describir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} es de tipo {self.tipo_cocina}")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} está abierto")

mi_restaurante = Restaurante('La Pizzería de Pepe', 'Italiana')

print(mi_restaurante.nombre_restaurante)
print(mi_restaurante.tipo_cocina)

mi_restaurante.describir_restaurante()
mi_restaurante.abrir_restaurante()