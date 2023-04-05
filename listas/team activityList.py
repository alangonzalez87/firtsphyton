numbers=[]

number = -1

while number != 0:
    number= int(input('write a number!\n'))
    
    if number !=0:
     numbers.append(number)


numbers_total=0
for number in numbers:    
 numbers_total+= number
        
print(f'la suma total es {numbers_total}')

conteo= len(numbers)
promedio= numbers_total / conteo
print(f'el promedio es {promedio}')