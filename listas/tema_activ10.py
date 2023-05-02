
print("please type the name account and balance, type quit to finish")


banks=[]
balances=[]

bank= None


while bank != "quit":
        bank=input("account:")
        

        if bank != "quit":
            balance=int(input("whats is the balance?"))
            
            banks.append(bank)
            balances.append(balance)

for bank in banks:
        print(f'your acount information is {bank}: {balance} ')