
class colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    WHITE = '\033[37m'

items=[]
item= None
prices=[]
total = 0
print("Bienvenidos a su carrito virtual por favor eliga una opcion:")

while True:
        print(colors.RED + '1:Agregar al carrito')
        print(colors.BLUE +'2:Ver el carrito')
        print (colors.GREEN +'3:Eliminar un item del carrito')
        print (colors.YELLOW +'4:Suma total')
        print('5:Salir')
        print()
        opcion=input('')
        if opcion == "1":
            item= input('desea agregar un producto?: ')
            price=float(input(f'Cual es el precio de {item}?: '))
#price= str(price)
            print( f"Usted agrego los siguientes productos a su carrito: {colors.RED + item} con un valor de $ { price} ")
            print('<--------------------------------->')
            if item in items:
                   print('ese item ya se encuentra en la lista')
            else:       
                items.append(item)
                prices.append(price)
        elif opcion == "2":
              print("*------------------------------*")
              for  i in range(len(items)):
               print (f'{colors.GREEN + items[i]} ${prices[i]}' )
               print("*------------------------------*")
               print()
        elif opcion == "3":
             print("*--------------------------------------*")
             #print(items[i])
             item= input("cual item desea cambiar?")
             
             print("*--------------------------------------*")
             #if opcion !="no":
             if item not in items:
                print("ese item no esta en la lista")
             else:
                items.remove(item)
             #print(f"desea cambiar {item} con un valor de {price}: si/no ")    
        elif opcion =="4":
 #           price=float(price)
            for i in prices:
                 #print(f"{i}.{items[i]} - $ {prices[i]} ")
                 total += i 
            print(f"la suma total hasta ahora es:{total}")     

        elif opcion =="5":
              print("gracias por comprar en Supermercados EL Corchete Feliz ")
              break
        else:
              print('debe poner la opcion correcta')
            

