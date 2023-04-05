import random 

secret = [ 'yemen', 'catar', 'tonga','india','rusia']
word = random.choice(secret)

guess= ''
game_loop = 0


print("""Bienvenido  el juego es simple puedes adivinar la palabra de 5 letras?
si la letra es correcta y esta en posicion incorrecta la letra saldra en minuscula
si la letra es correcta y esta en posicion correcta te saldra en mayuscula
entendido? comencemos""")

print('your hint is: ', end=' ')
#init game
for letter in word:
    print('_', end=' ')
print()

while word != guess:
        game_loop+=1 
        print(f'the word have {len(word)} letters')
        guess = input('puedes encontrar la palabra escondida?\n')

        for i, letter in enumerate(guess.lower()):

            if i < len(word) and letter == word[i]:
                    
                 print(letter.upper(), end=' ')

            elif letter in word:
                    print(letter.lower(), end=' ')
                
            else:
                    print('_', end=' ')
                    print()
               
print(f'excelente te tomo {game_loop} intentos')

# for i in range (5):
#     print (" ".join(board[i]))

# while guess.lower() != word.lower():
    
#     for i in range(word.__len__()):
       
#         if guess[i] == word[i]:
#              output = guess[i]
#              print(output.upper(), end=" ")

#         elif guess[i] in word:
#              output = guess[i]
#              print(output.lower(), end=" ")
#         else:
#              output = guess[i]
#              print('_'*5, end=' ')
#              print()
#     hint = hint+1         
#     guess = input('puedes encontrar la palabra escondida?\n')
                
# else:
#     print(f'excelente te tomo {hint} intentos')


# for i in range(word.__len__()):
#             if user_input[i] == word[i]:
#                 output = user_input[i]
#                 print(output.upper(), end=' ')
#             elif user_input[i] in word:
#                 output = user_input[i]
#                 print(output.lower(), end=' ')
#             else:
#                 output = user_input[i]
#                 print('_', end=' ')