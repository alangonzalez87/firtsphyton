with open('archivos/hr_system.txt') as datos:

    for dato in datos:
        variable = dato.split(' ')
        

        nombre= variable[0]
        id=variable[1]
        trabajo=variable[2]
        salario=float(variable[3])

        print(f'nombre: {nombre} (id: {id}) trabajo: {trabajo}- salario:${salario:.2f}')