class Restaurante:
    def __init__(self, nombre, tipo):
        self.nombre_restaurante = nombre
        self.tipo_cocina = tipo

    def describir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} es de tipo {self.tipo_cocina}")

    def abrir_restaurante(self):
        print(f"El restaurante {self.nombre_restaurante} está abierto")

class carritoDeHelados(Restaurante):

    def __init__(self, nombre, tipo, sabores):
        super().__init__(nombre, tipo)
        self.sabores = sabores

    def mostrar_sabores(self):
        print("Sabores disponibles:")
        for sabor in self.sabores:
            print(f"- {sabor}")


mi_carrito = carritoDeHelados('El Carrito de Pepe', 'Helados', ['Chocolate', 'Vainilla', 'Fresa'])
mi_carrito.mostrar_sabores()