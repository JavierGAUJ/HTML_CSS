def decora(f):
    def envuelve():
        print('estoy a punto de ejecutar la funcion')
        f()
        print('termine de ejecutar la funcion')
        return envuelve

@decora
def hola():
    print('hola mundo!')


hola()
