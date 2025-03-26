'''
if anidados:
if dentro de otro if 
syntax:
if condicion1:
   if condicion2
   print ("mensaje")
if condicion3: 
'''
#ejemplo 1:
#Modifique el ejercicio de la edad 
#para las siguientes condiciones 
# 1. si es mayor de 18 años 
#pero no tiene documento no puede votar 
#de lo contrario si se puede votar
#2. si es menor de 18 años
#no puede votar 
#utlize estructurar de if anidados
edad = int (input ("digite su edad:"))
if edad >= 18:
    documento = input ("tiene documento si/no?:")
    if documento == "si":
        print ("ud puede votar")
    else:
        print ("ud no puede votar")

else:
    print("ud no puede votar")
 