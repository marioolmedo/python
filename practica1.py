notas = []
x= int(input("Ingrese cantidad de notas: "))
for x in range(x):
    nota = 0
    while nota <1 or nota >5:
        nota = int(input(f"Nota {x+1}:"))
        
    notas.append(nota)
    
suma=0
for x in range(len(notas)):
    suma = suma + notas[x]
    
promedio = suma / len(notas)
print(f"Promedio: {promedio}")

if (promedio > 1.7):
    print("Aprobado")
else:
    print("Reprobado")