lista = [1,2,3,4]

for i in lista:
    print(i*2,end=" ")
print()    
for i in range(len(lista)):
    print(i*3,end=" ")
print()
for pos,valor in enumerate(lista):
     print(pos,valor,end=" ")
print()    
nueva_lista = [ i*5 for i in lista]
print(nueva_lista)
print("*"*20,"Diccionario","*"*20)
diccionario = {
        1:"Hola",
        2:"Como estas",
        3:"Bien"
    }
resultado = diccionario.get(0,"No existe un valor asociado a esta clave o no existe esta clave")
print(resultado)
diccionario[4] = "Que bueno"


for clave,valor in diccionario.items():
    print("{0} --> {1} ".format(clave,valor))
    

for clave in diccionario:
    resultado = diccionario.get(clave,"No existe un valor asociado a esta clave o no existe esta clave")
    print(clave,resultado)

for clave in diccionario.keys():
    print(clave)

print("conjuntos")
cadena = "Esto es un hola desde consola"
cadena = set(cadena)
print(cadena)