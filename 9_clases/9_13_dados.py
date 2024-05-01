from random import randint
class Dados:
    def __init__(self, caras=6):
        self.caras = caras

    def lanzar(self):
        return randint(1, self.caras)
    

dado = Dados()
count = 0

print("Dado de 6 caras")

while count < 10:
    print(dado.lanzar())
    count += 1
    
dado_diez = Dados(10)
count = 0

print("Dado de 10 caras")

while count < 20:
    print(dado_diez.lanzar())
    count += 1