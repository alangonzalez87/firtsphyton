import math
def compute_area_square(side):
        return side * side


def compute_area_rectangle(side,lengh):
    return side * lengh

def compute_area_circle(radius):
    return math.pi * radius * radius


forma= ""

while forma != 'quit':
   # print("""eliga la forma para hacer la cuenta respectiva, escriba salir para terminar el programa \n""")
    user=input("que forma tiene? cuadrado, circulo, rectangulo?\n")
    
    forma=forma.lower()

    if user == "cuadrado":
        numero = float(input('cual es el area?'))
        numero= compute_area_square(numero)
        print(numero)
    
    if user =="rectangulo":
         largo= float(input('escriba el largo del rectangulo:'))
         ancho= float(input('escriba el ancho del rectangulo:'))

         total= compute_area_rectangle(largo,ancho)
         print(total)
    if user=="circulo":
         radio= float(input("cual es el radio del circulo?:\n"))
         radio=compute_area_circle(radio)
         print(radio)
    else:
         print("gracias por usar nuestra calculadora")
        

        
        
