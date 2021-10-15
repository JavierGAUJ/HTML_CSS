class vuelo:
    def __init__(self, capacidad): 
        self.capacidad = capacidad
        self.pasajeros = []


def getDisponibles(self):
            return self.capacidad - len(self.pasajeros)


def addPasajero(self, nombre):
    if self.getDisponible():
         self.pasajeros.append(nombre)
    else:
             return False
vuelo = vuelo(3)

personas = ['paulina', 'moises', 'hector', 'balam', 'raul', 'joeclyn']

for persona in personas:
    if vuelo.addpasajero(persona):
        print(f'se agrego a {persona} al vuelo')
    else:
        print('no se agrego')
        print(vuelo.getDisponibles())
vuelo.addpasajero('javier')