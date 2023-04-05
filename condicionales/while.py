
palabra= 'gatos'
intentos= 0

palabra=input('puedes adivinar la palabra escondida?\n')



while palabra != 'gatos' :
    intentos = intentos + 1
    
    palabra=input('puedes adivinar la palabra escondida?\n')
    if palabra != 'gatos':
        print(' otra vez')
    else:
        print('perfecto')
        
print(f'te llevo { intentos }')        
    
