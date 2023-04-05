# Here we have the colors class.
class colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    WHITE = '\033[37m'
print()
#Welcome.
print ('WELCOME TO CSE 110')
print()
#Welcame question.
volunt = input ("Can you response a question? (y/n) ")
print()
#Answer option to yes response
if volunt == ('y'):
     print("Please select your favorite color of this: ")
     print()
     print(colors.BLUE + "1- Blue  " + colors.RED + "2- Red  " + colors.YELLOW + "3- Yellow  " + colors.GREEN +"4- Green" )
     print()
     color = input(colors.WHITE + 'Enter the number of the color: ')
     print()
# Answers options for colors selected
     if color == ('1') : print(colors.BLUE + color + " is a amazing color.")   
     if color == ('2') : print(colors.RED + color + " is a amazing color.")
     if color == ('3') : print(colors.YELLOW + color + " is a amazing color.")
     if color == ('4') : print(colors.GREEN + color + " is a amazing color.")
     else:print("This is not a option")
     print()
     print(colors.WHITE + "Thanks for your time!! See you :)")
     print()
#Answer option to no response    
else:
    print (colors.RED + "ok, no problem :( " + colors.WHITE)
    print()