import csv
small_num=9999.999
highest=0


with open ('archivos/life-expectancy.csv') as excel:
     reader=csv.reader(excel)

     for line in reader:
        for list in excel:
         datos= list.strip().split(",")
         country=datos[0]
         sigla=datos[1]
         year= int(datos[2])
         aver =float(datos[3])

         if float(datos[3]) > 0 and aver < small_num:
            small_num = aver
            pais = country
            anio= year
         if float(datos[3]) > 0 and aver > highest:
            highest= aver
            pais_max = country
            annio_max= year
        print(f'min es {small_num} en {pais} en el year{anio}')
        print(f'max es {highest} en {pais_max} en el year{annio_max}')