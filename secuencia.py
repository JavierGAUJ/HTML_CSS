
nombre = 'paulina'
print(nombre[0])
nombres = ['Paulina', 'Moises', 'Hector', 'Balam', 'Raúl', 'Jocelyn']
print(nombres)

nombres[0] = 'Max'
print(nombres)

nombres.sort()
print(nombres)

nombres.append('paulina')
nombres.reverse()
print(nombres)

# Tuplas
tupla = (1, 2, 3, 4, 5, 3, 5)

print(tupla)
print(tupla.count(3))
print(tupla.index(3))
#tupla[0] = 23

# set
#https://docs.python.org/3/tutorial/datastructures.html#sets
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)

print(s)

s.remove(3)

print(s)

s.add(2)
s.add(2)
s.add(2)

print(s)

#diccionario
edades = {'Paulina', 'Moises', 'Hector', 'Balam', 'Raúl', 'Jocelyn'}

print(edades)
print(edades['Jocelyn'])

edades['Raul'] =20
print(edades)

edades['Balam'] +=1
print(edades)

#Listas(arreglos) - secuencia mutable de variables
#tuplas - secuencia no mutable de variables
#set - colecccion de valores unicos
#diccionarios - coleccion de pares llave-valor


