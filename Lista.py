calificaciones = [1, 2, 3, 4, 5]
nombres = ["Moises","Fernanda", "Pablo", "Tania", "Moises"]
lista_var = [True, 10.5, "abc", [0,1,2]]

print("Estudiante: ", nombres[1])
print("Calificación: ",calificaciones[2])
print("Lista dentro de otra: ", lista_var[3][0])
print("Imprimir un rango o slices: ", nombres[1][2])
print(lista_var)

#agregar elementos a una lista
nombres.append("Anibal")
print(nombres)
#remover nombres de una lista
nombres.remove("Pablo")
print(nombres)
