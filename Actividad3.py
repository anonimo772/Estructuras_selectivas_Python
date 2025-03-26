'''
elabore un programa que 
permita calcular el salario
neto de un empleado,
Despues de descontar 
los descietos por conceptos de:
Salud, Pension, ARL
1,El programa debe solicitar
el tipo de empleado:
   a-contrato a termino indefinido
   b-Contrato pro prestacion de servicios 
   c-Contrato de aprendizaje 
   d-Contrato por jornal(FREELANCE) 
'''
contrato = input ("ingrese el tipo de contrato:")
salario_neto =  0
if contrato == "a":
    print ("eligio: contrato a termino indefinido")

elif contrato =="b":
    print ("eligio contrato por prestacion de servicios")
    
elif contrato =="c":
    print ("eligio contrato de aprendizaje")
    salario_minimo = int (input ("ingrese el valor de su salairo minimo:"))
    salario_neto = salario_minimo * 0.75
    
elif contrato =="d":
     print ("eligio jornal")
     #variable local
     #variable que solo se utiliza
     #en un bloque de codigo
     numero_horas = int(input ("ingrese numero de horas:"))
     valor_hora = int(input ("ingresa el valor x hora a pagar:"))
     salario_neto = numero_horas *valor_hora
else:
    print ("tipo de contrato no existe")
print ("salario neto es:", salario_neto)
print ("fin del programa")
    