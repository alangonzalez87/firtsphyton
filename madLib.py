name= input("please enter your name")

adjetive=input("please choice a adjetive:")

verbs=input ("please choice a verbs:")

animal= input ("please choice a animals:")

verbs2= input("please choice other verbs:")

verbs3= input("please choice other verbs:")

adjetive2=input("please choice another adjetive:")

exclamation= input ("please choice a exclamation:")

exclamation2= input ("please choice another exclamation:")

list= (f"{adjetive}  {verbs} {verbs2} {verbs3} {animal}  {verbs2}  {exclamation} {adjetive2} {exclamation2}")

print(list)
print("------------------------------------")

print('Ahora esta es tu historia...')

print("------------------------------------")

print('The ' + adjetive +' dog was so ' + verbs + ' that it ' + animal+ ' its tail and ' + verbs2 + ' happily. But when it saw the '
     + exclamation + ' cat, it began to '+ verbs3 + ' fiercely.\n The cat, who was quite ' + adjetive2 + ' too,' + verbs + ' back and the two animals '
     + verbs3 + ' around the room.\n Suddenly, the owner of the house, ' + name.capitalize() + ' shouted ' + exclamation.upper() + ' and ' + exclamation2.upper()
     + ' as she tried to stop the fight and they runs.')