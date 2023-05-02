import random



invitado = 'yes'

while invitado:
    number_magico = random.randint(1,10)
    
    intentos=0

    intentos_inv = -1

    while intentos_inv != number_magico:
        intentos_inv=int (input('puedes adivinar el numero magico?\n'))
       
        intentos += 1
       
        if intentos_inv < number_magico:
            print('mas alto')
        elif intentos_inv > number_magico:
            print ('mas bajo')
        else:
            print('adivinaste!')
    print(f'te costo: {intentos}')
    invitado = input('queres jugar de nuevo?\n yes/no: ')
    if invitado == "no":
        print('see you later my friends!')
        break


