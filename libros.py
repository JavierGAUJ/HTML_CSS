libros = [
    {'Titulo': 'El principito', 'año':1943},
    {'Titulo': 'El arte de la guerra', 'año': 1773},
    {'Titulo': 'La ciudad de las bestias', 'año':2002},
    {'Titulo': 'El hobbit','año':1984},
    {'Titulo': 'La grita','año': 2007}
    ]
libros.sort(key='año')
#libros.sort()
#no podemos coparar objetos sin decir algo más :
#libros.sort(key='año')
#sort no sabe que debe buscar dentro del diccionario
def ftitulo(libro):
    return libro['Titulo'].upper()
def fanio(libro):
    return libro['año']

#print(ftitulo(libros[0]))
#print(fanio(libros[0]))
print(libros)
print()

#print('libros ordenados año:')
#libros.sort(key=ftitulo)
#print(libros)

#print('libros ordenados por titulo:')
#libros.sort(key=ftitulo)
#print(libros)

libros.sort(key=lambda libro:libro ['año'])
for libro in libros:
    #print(f"el libro {libro ['titulo']} fue publicado en {libro['año']}")
    print('el libro {titulo} fue publicado en {año}'. format(**libro))
    #  #print(libros)

libros.sort(key=lambda libro:libro['titulo'])
#print(libros)