
class Validar:
  def __init__(self):
    self.valor = ""
  def numeros(self,mensaje,error):
    try:
      self.valor = int(input(mensaje))
      return self.valor
    except ValueError:
      print(error)
      self.numeros(mensaje,error)
      
  def decimales(self,mensaje,error):
    valor=0
    try:
      self.valor = float(input(mensaje))
      return self.valor
    except ValueError:
      print(error)
      self.decimales(mensaje,error)
  
  def letras(self,mensaje,error):
    try:
      self.valor = input(mensaje)
      if self.valor.isalpha():
        return self.valor
    except:
      print(error)      
    else:
      print(error)
      self.letras(mensaje,error)
          
  
val  = Validar()
#val.numeros("Ingrese numero entero","error debe ingresar solo digitos")  
x = val.decimales("Ingrese Sueldo: ","error debe ingresar solo numeros")  
#x = val.letras("Ingrese Nombre: ","error debe ingresar solo letras")  
print(val.valor)