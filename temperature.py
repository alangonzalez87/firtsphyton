import math

#temperature en farenheit

Farenheit= input ('whats is the actual temperature? please respond in farenheit: ')
newTem= int( Farenheit)
celsius= (newTem - 32) * 5/9

print(f'today is  :{celsius:.1f} in celsius')