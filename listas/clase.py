friends=[]
name=None


while name != "end":
    name= input('whats is the name of your friend?\n')
    
    if name != "end":
        friends.append(name)
print()
print("your friends are: ")
for friend in friends:
    print(friend)
