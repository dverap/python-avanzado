def multiplicar(inicio,*args,**kwargs):
    print(kwargs)
    for i in args:
        inicio += i
    return inicio

print(multiplicar(0,2,4,6,8,10,resultante = 200,cancelacion = 50))
