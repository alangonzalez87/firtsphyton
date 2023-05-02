import math


#Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)
def viento_temperatura(t,v):
    wind_chill = 35.74 + (0.6215*t) - (35.75*(v**0.16)) + (0.4275 * t * (v**0.16))
    return wind_chill
def conversion(t):
    f = (t * 9/5) + 32
    return f

while True:
    user= input("Fahrenheit or Celsius (F/C)?")
    user=user.lower()

    if user == "f":
        t=float(input('cual es la temperatura en f?'))
        for v in range (5,65,5):
            resultado=viento_temperatura(t,v)
            print(f'At temperature {t}F, and wind speed {v} mph, the windchill is:{resultado:.2f}F')
       

    if user == "c":
        t=float(input('cual es la temperatura en C ?'))
        
        for v in range (5,65,5):
            cambio=conversion(t)
            resultado=viento_temperatura(cambio,v)
            print(f'At temperature {cambio}F, and wind speed {v} mph, the windchill is:{resultado:.2f}F')
        
        


