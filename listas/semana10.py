# books=["harry", "pedro", "juan"]

# for i in range(len(books)):
#     book = books[i]
#     print(f"{i}.libro: {book}")


items=[]
item= 1
print("Please enter the items of the shopping list (type: quit to finish):")

while True:
    print("1: add items")
    print("2: ver carrito")
    print("3:cambiar un item del carrito")
    print("4: quit")
    opcion=input('')
    print()
    if opcion.lower() == "add":
                item = input('desea agregar un producto?')
                print()
               
                if item in items:
                    print('ese item ya se encuentra en la lista')
                else:       
                    items.append(item)

    elif opcion.lower() == "ver":
                print('\n the list is:')
                for i in range(len(items)):
                    item= items[i]
                    print(f"{i}.{item}")
                    print("---------------------------------")
    elif opcion.lower() =="quit":
                print("gracias por comprar en Supermercados Francia segundo ")
                break
    

    elif opcion.lower() == "cambiar":
        item=input('cual item desea cambiar?')
        if item not in items:
                    print('ese item ya se encuentra en la lista')
        else:
                    items.remove(item)
                    print("---------------------------------")
    else:
                print('debe poner la opcion correcta')             
                         


