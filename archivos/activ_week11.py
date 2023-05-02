import csv


esperanza_alta=9999.999
esperanza_baja=-1


with open ('archivos/life-expectancy.csv') as excel:
     reader=csv.reader(excel)

     for line in reader:
      for list in excel:
         datos= list.strip().split(",")
         country=datos[0]
         sigla=datos[1]
         year= int(datos[2])
         esperanza =float(datos[3])
         if  float(datos[3]) > 0 and esperanza < esperanza_baja:
            esperanza_baja = esperanza
            pais = country 
            anio=year
         if float(datos[3]) > 0 and esperanza > esperanza_alta:
           esperanza_alta = esperanza
           pais_max = country
           anio_max=year
           print(f'la esperanza de {esperanza_baja} {pais} en el {anio}')
           print(f'la esperanza mas alta es de {pais_max} con {esperanza_alta} en el {anio_max}')
           
               

#Fuente: https://www.iteramos.com/pregunta/77334/leer-columnas-especificas-de-un-archivo-csv-con-python-csv
                
            
               

       
 









