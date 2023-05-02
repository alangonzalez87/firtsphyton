#el hombre en el bosque!!!
#primera parte!
historia= """el hombre salio corriendo desesperado por el bosque...la criatura le seguia, solo podia escuchar el rugir de sus dientes y sus tenebrosos pasos
que monstruo tenebroso te gustaria que lo siga?

(1) hombre lobo feroz malo malo
(2) Jinete sin cabeza

"""
print(historia)

print('--------------------------------')

ask1=input('')
if ask1 == '1':
    historia2="""el hombre lobo lo seguia de cerca casi tan cerca que podia saborear su transpiracion que corria de su piel, de repente el hombre escucha que alguien lo llamaba...
    quien lo llama?
    (1) su mama a comer
    (2) el lobo aprendio su nombre
    (3) un desconocido que lo vio y pensaba que hacia running (si, en el bosque y a medianoche)"""
    print(historia2)
    print("-"*30)
    
    rta=input('')
    if rta==('1'):
         print('de repente se desperto')
    elif rta ==('2'):
        print('oh no los lobos dominaran el mundo!')
    elif rta ==('3'):
        historia3="""El desconocido huyo tan rapido como pudo, tan rapido que se olvido de su auto al costado de la ruta, en ese instante...
            (1)oyo un bocinazo del lobo con su auto 
            (2) el primer hombre lo alcanza y corren juntos 
            (3) el primer hombre tambien se transforma en hombre lobo"""
    else:
        print('tienes que elegir 1, 2, 3 para continuar la historia...')
      
        
elif ask1=='2':
    print('el jinete lo mato...')
else:
    print('tienes que elegir un monstruo')


