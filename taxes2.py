class colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    WHITE = '\033[37m'


# ask the user the prices of meals
print ( colors.BLUE + "What is the price of a child's meal?")
meals1= float (input('please enter a number:'))
#price1= float(meals1)

print ( colors.YELLOW + "What is the price of an adult's meal?")
meals2= float(input ('please enter a number:'))
#price2= float (meals2)

#ask for the cuantity

print ( colors.GREEN + "how many childrens are there?")
child= int(input ('please enter a number:'))
#cuantity_of_children= int(child)

print ( colors.YELLOW + "how many adults are there?")
adults= int(input('please enter a number:'))
#cuantity_of_adults= int(adults)

#sales rate 

print( colors.RED + "What is the sales tax rate?")
sales= float(input ('please enter a number:'))

print("--------------------------------")
#calculate subtotal 

currency= "$"

subtotal = float (meals1 * child) + (meals2 * adults)
print (colors.GREEN + f'subtotal: {currency} {subtotal}')


taxes=float(subtotal * sales) / 100
print(f'total taxes: {currency} {taxes:.2f}')
finishpayment= float (taxes + subtotal)
print()

print(f'the total payment is {currency} {finishpayment:.2f}')

amount=float(input('whats is the payment amount? :'))

change=float(amount - finishpayment )

print(f'Your change is : {currency} {change:.2f}')


