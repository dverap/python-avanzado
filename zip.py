lista = [1,2,3,4,5,6,7,8,9,10]
tupla = ('hola','Perú','Developer.pe','Facebook','Twitter')
lista2 = ['12','13','14',(9,8,7)]

union = tuple(zip(lista,tupla,lista2))
print(union)

nombres = ["Daniel","Yady","Erick"]
apellidos = ["Papa","Mama","hijo"]
edades = [52,50,4]
print(list(zip(nombres,apellidos,edades)))
print(dict(zip(nombres,apellidos)))
