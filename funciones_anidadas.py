def primera_funcion(valores):
    print(valores)

    def iterar_valores():
        for i in valores:
            print(i,end=" ")
        
        def funcion_tercera():
            print("Hola desde la tercera funcion")
        print()
        funcion_tercera()

    iterar_valores()       
    
primera_funcion([1,2,3,4,5,6,7])