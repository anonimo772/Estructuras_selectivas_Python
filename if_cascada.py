'''
if en cascada
es una estructura selectiva 
conpuesta pro multiples condicionales
seguidos unos de otros
sintaxis:
elif condicional 1:
    instruccion 1
    instruccion 2
elif condicional 2 :
    instruccion 3
    instruccion 4
elif condicional 3:
    instruccion 5
    instruciion 6
CADA CONDICIONAL ES MUTUAMENTE EXCLUYENTE

'''
#ejemplo
#vamos a hacer un pequeño
#traductor
#el programa debe permitir 
#leer una fruta en español y debe mostrar esa fruta
# en ingles  
fruta = input ("ingrese el nombre de una fruta:")
if fruta == "manzana" or fruta == "manzana":
    print("apple")
elif fruta == "naranja" or fruta == "manzana":
    print ("orange")
elif fruta == "uva" or fruta == "uva":
    print ("grape")
elif fruta == "banano" or fruta == "banano":
    print ("banana")
#caso por defecto
else:
    print ("esa palabra no esta en el diccionario")