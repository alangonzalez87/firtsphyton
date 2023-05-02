import csv
mayor_esperanza=0
baja_esperanza=9999.99
promedio=0
contador=0


search = int(input("What is the year of interest " ))
with open ('archivos/life-expectancy.csv') as excel:
     reader=csv.reader(excel)
     for line in reader:
          for list in excel:
               data= list.strip().split(",")
               pais=data[0]
               abreviatura=data[1]
               year=int(data[2])
               hope=float(data[3])
               if year == search:
                    promedio += hope
                    contador+=1
                    
                    if baja_esperanza > hope:
                        baja_esperanza = hope
                        pais_max = pais
                        anio_max=year
                    if mayor_esperanza < hope:
                        mayor_esperanza= hope
                        pais_min = pais
                        anio_min =year
average=promedio/contador
print(f"promedio mundial {average:.2f}" )
print(f'Hope:{baja_esperanza} country:{pais_max} year:{anio_max}')
print(f'Hope:{mayor_esperanza} country:{pais_min} year:{anio_min}')                         