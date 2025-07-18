lista = []
def cargarContenido(dato):
    lista.append(dato)

def imprimirlista():
    print(lista)

def quitardelista(dato):
    lista.remove(dato)

if __name__=="__main__":
    cargarContenido("Yo soy")
    cargarContenido("Groot")
    imprimirlista()
    quitardelista("Groot")
    cargarContenido("una persona")
    imprimirlista()
