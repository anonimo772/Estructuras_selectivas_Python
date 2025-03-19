'''
sintaxix
if condicional;
  instruccion1
  instruccion2
else
instruccion3
instruccion4
'''


#ejemplo
#elabore un programa
#que determine si una persona 
#es mayor o menor de edad y por tanto habilitar
#votar

edad = 17 
Documento = True
if edad >= 18 and Documento==True:
    print ("ud es mayor de edad")
    print ("puede votar")

else: 
    print ("ud es menor de edad")
    print ("no puede votar") 
print ("final del programa")