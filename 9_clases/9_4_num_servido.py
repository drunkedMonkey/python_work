class Restaurante:
    def __init__(self, nombre, tipo):
        self.nombre_restaurante = nombre
        self.tipo_cocina = tipo
        self.num_servido = 0

    def describir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} es de tipo {self.tipo_cocina}")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} está abierto")

    def establecer_num_servido(self, num):
        self.num_servido = num

restaurante = Restaurante('La Pizzería de Pepe', 'Italiana')
restaurante.num_servido = 10
print(restaurante.num_servido)

restaurante.establecer_num_servido(20)
print(restaurante.num_servido)