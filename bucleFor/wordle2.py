word='commitment'

pregunta= input('cual es tu letra favorita?')

for letter in word:
    if letter.lower() == pregunta.lower():
        print(letter.upper(),end="")
    else:
        print(letter.lower(),end="")
print()

for letter in word:
    if letter.lower() == pregunta.lower():
        print("_",end="")
    else:
        print(letter.lower(),end="")
print()