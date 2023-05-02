def display_regular(name):
        output= name
        return output


def display_uppercase(name):
    new_name = name.upper()
    print(new_name)
    

def display_lowercase(name):
        new_name = name.lower()
        print(new_name)


nombre= input('escriba un texto largo: \n')
display_regular(nombre)
display_uppercase(nombre)
display_lowercase(nombre)

