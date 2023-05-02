import random

palabra = ['book', 'read', 'word']

secret= random.choice(palabra)


preg= str(input('puedes adivinar la palabra escondida?\n'))



while preg.lower() != secret.lower():
            
        for i in range(secret.__len__()):
            
            if preg[i] == secret[i]:
                output = preg[i]
                print(output.upper(),end=" ")
            elif preg[i] in secret:
                output = preg[i]
                print(output.lower(), end=" ")
            else:
                output = preg[i]
                print('_'*4, end=" ")
            
            print()
            preg=input('puedes adivinar la palabra escondida?\n')
else:
     preg.lower() == secret.lower()
     print('perfecto adivinaste la palabra escondida')



