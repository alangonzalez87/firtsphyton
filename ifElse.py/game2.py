historiaAmor = "La excelente y lamentable tragedia de Romeo y Julieta, Cuenta la historia de dos jóvenes que, a pesar de la oposición de sus familiares, rivales entre sí, deciden casarse de forma ilegal y vivir juntos; sin embargo, la presión de esa rivalidad y una serie de fatalidades conducen a que la pareja elija el suicidio antes que vivir separado"
historiaAmor2="al final de la historia julieta despierta de su sueño profundo justo antes de que Romeo tome el cianuro y evitando el suicidio, Entonces deciden escapar a Argentina y ser felices para siempre fin..."

historiaTerror="haha is not a history  "

print('Welcome to Game Adventures please select a history')
menu= """Choice between love  or terror """
print(menu)
ask1= input('')
if ask1.lower() == 'love' :
    press = int(input('Good choices, press 1 to start:'))
    if press == 1:
        print(historiaAmor)
    else:
        print('come back later when you want to read')
elif ask1.lower()== 'terror':
    press = int(input('terrorific choices, press 2 to start:'))
    if press == 2:
       print(historiaTerror)
    else:
        print('come back later when you want to read')
else:
    print('vuelve a elegir la historia')

ask2= input('do you want to change the end of this tragedy history?\n yes / no \n')
if ask2.lower()== 'yes':
    print(historiaAmor2)
else:
    print('the love always is tragic')

