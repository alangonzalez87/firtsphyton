people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
mas_joven= 99999
nombre_joven= ''
for person in people:
    line= person.split()
    nombre=line[0]
    edad=int(line[1])
    if edad < mas_joven:
        mas_joven=edad
        nombre_joven=nombre
print(f'el nombre es {nombre_joven} y su edad {mas_joven}')


