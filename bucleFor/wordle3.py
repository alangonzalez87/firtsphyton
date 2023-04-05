#Carol Wordle...
import random
import time
import sys

def mec(texto):

 lista = texto.split()

 for palabra in lista:
    sys.stdout.write(palabra + " ")
    sys.stdout.flush()
    time.sleep(0.2)

mec('welcome to secret animal gusses game!!.\n')
print()
mec('enter a 3 letters animal!.\n')
print()
animal= (['dog','cat','pig', 'fox', 'cow','ant'])
number=1
secret= random.choice(animal)

guess= input('What is your animal guess? ')

while len(secret) != len(guess):
     print('Sorry your word not have 3 letters')
     print('Try again...')
     guess= input('What is your animal guess? ')

else:
     while guess.lower() != secret.lower() and len(secret) == len(guess):
         for i in range(secret.__len__()):
            if guess[i] == secret[i]:
                output = guess[i]
                print(output.upper(), end=' ')
            elif guess[i] in secret:
                output = guess[i]
                print(output.lower(), end='')
            else:
                output = guess[i]
                print('_', end=' ')

         print('Try again...')
         number = number + 1
    
         guess = input("Input another word: ")

         while len(secret) != len(guess):
             print('Sorry your word not have 3 letters')
             print('Try again...')
             guess= input('What is your animal guess? ')
            
     else:
         guess.lower() == secret.lower()
         print()
         mec('Congratulation your guess is correct!')
         print()
         #print(f'You try {number} times to guess')​
#Contraer

