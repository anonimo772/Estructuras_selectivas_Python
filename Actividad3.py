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
   ==>
   se debe solicitar 
   -numero de horas trabajadas
   -el valor a pagar por hora 
   -el total de salario se calcula de multiplicar 
   el numero de horas por el valor a pagar por hora
   ==> para el caso de prestasion de servicios 
   se debe solicitar:
   - el valor del contrato 
   -el numero de meses del contrato
   -la antiguedad del empleado(años)
   1- dividir el valor del contrato 
   por el numero de meses
   2-resta el 0,15% del valor anterior
   por concepto de eps
   3-restar el 10% del salario mensual
   por concepto de pension 
   4-si el empleado posee una antieguaedad igual o mayor a 
   10 años  tendra una bonificacion del 0.5% sobre el valor mensual 
   ==>PARA EL CONTRATO DE TIEMPO INDEFINIDO SE DEBE
   SOLICITAR:
   -antiguedad (años)
   -grado o escalafor (1 - 5)
   El salario neto se calcula de acuerdo a la 
   siguente tabla:
    Grado 1: 1.5 5M
    Grado 2: 1.7 5M
    Grado 3: 2.0 5M 
    Grado 4: 2.5 5M
    Grado 5: 3.0 5M
    La bonificacacion estara acorde 
    a los sigueintes rangos segun la antiguedad
    -Entre 1 y 5 Años: 1% salario mensual
    -Entre 6 y 10 Años: 2% salario mensual
    -Superior a 10 Años: 3%  salario mensual
    Para este caso los descuentos del ley son
    25% por conceptio de eps 
    22% por concepto de 
    0.1% Por concepto de ARL 
'''
# Solicitar el tipo de contrato
contrato = input("Ingrese el tipo de contrato (a: Indefinido, b: Prestación de servicios, c: Aprendizaje, d: Jornal): ")

# Definir el salario neto
salario_neto = 0

if contrato == "a":
    print("Eligió: contrato a término indefinido")
    antiguedad = int(input("Ingrese la antigüedad del empleado (en años): "))
    grado = int(input("Ingrese el grado (1-5): "))
    
    if grado == 1:
        salario_mensual = 1.5 * 5_000_000
    elif grado == 2:
        salario_mensual = 1.7 * 5_000_000
    elif grado == 3:
        salario_mensual = 2.0 * 5_000_000
    elif grado == 4:
        salario_mensual = 2.5 * 5_000_000
    elif grado == 5:
        salario_mensual = 3.0 * 5_000_000
    else:
        print("Grado no válido.")
        salario_mensual = 0
        
    if antiguedad <= 5:
        bonificacion = salario_mensual * 0.01
    elif antiguedad <= 10:
        bonificacion = salario_mensual * 0.02
    else:
        bonificacion = salario_mensual * 0.03
    salario_neto = salario_mensual + bonificacion
    eps = salario_neto * 0.25
    pensiono = salario_neto * 0.22
    arl = salario_neto * 0.001
    salario_neto -= (eps + pensiono + arl)

elif contrato == "b":
    print("Eligió contrato por prestación de servicios")
    valor_contrato = int(input("Ingrese el valor del contrato: "))
    numero_meses = int(input("Ingrese número de meses: "))
    antiguedad = int(input("Ingrese antigüedad del empleado (en años): "))

    salario_mensual = valor_contrato * numero_meses / 12
    
    if antiguedad <= 5:
        bonificacion = salario_mensual * 0.01
    elif antiguedad <= 10:
        bonificacion = salario_mensual * 0.02
    else:
        bonificacion = salario_mensual * 0.03
    
    salario_neto = salario_mensual + bonificacion

    eps = salario_neto * 0.15
    pensiono = salario_neto * 0.10
    bonificacion_servicios = salario_neto * 0.05
    salario_neto -= (eps + pensiono)
    salario_neto += bonificacion_servicios

elif contrato == "c":
    print("Eligió contrato de aprendizaje")
    salario_minimo = int(input("Ingrese el valor de su salario mínimo: "))
    salario_neto = salario_minimo * 0.75

elif contrato == "d":
    print("Eligió jornal")
    numero_horas = int(input("Ingrese número de horas: "))
    valor_hora = int(input("Ingrese el valor por hora: "))
    salario_neto = numero_horas * valor_hora

else:
    print("Tipo de contrato no existe.")

print("Salario neto es:", salario_neto)
print("Fin del programa.")
    