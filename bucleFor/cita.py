quote= "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

respuesta='yes'


while respuesta == 'yes':
    run= int(input('eliga un numero:\n'))
    for i, letra in enumerate(quote):
        if i % run == 0:
            print(letra.upper(), end="")
        else:
            print(letra.lower(), end="")
print()

respuesta = input("Would you like to enter another number? ")

print ("Goodbye")