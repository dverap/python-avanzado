# decorador: agrega funciones extras a una funcion sin cambiar el codigo original de la misma
# recibe como parametro a la funcion que va a decorar 
# retorna una funcion nueva que esta dentro del decorador sino retorna una funcion da error
def funcion_decoradora(funcion):
    def nuevas_funcionalidades():
        print("Nivel 1 => Curso De Logica De Programacion")
        print("Nivel 2 => Curso De Fundamentos De Programacion")
        funcion()
        print("Nivel 4 => Curso De Programacion Orientada A Objetos")
    return nuevas_funcionalidades

def decoradora_multiplicar(funcion):
    def nuevas_funcionalidades(*args,**kwargs):
        x = 2
        resultado = funcion(*args,**kwargs)
        resultado = resultado * x
        print(resultado)
    return nuevas_funcionalidades


@funcion_decoradora # siempre se coloca al inicio de la funcion a decorar
def curso():
    print("Nivel 3 => Curso De Estructura De Datos")
    
curso()

@decoradora_multiplicar # siempre se coloca al inicio de la funcion a decorar
def multiplicar(num1,num2):
    return num1*num2
    
multiplicar(10,5)


