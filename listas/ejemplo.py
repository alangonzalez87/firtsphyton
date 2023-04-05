print("Please enter the items of the shopping list (type: quit to finish):")

shopping_list = []
item = None

while item != "quit":
    item = input("Item: ")

    if item != "quit":
        shopping_list.append(item)

# We now have the list. Print it out to verify:
print("\nThe shopping list is:")
for item in shopping_list:
    print(item)