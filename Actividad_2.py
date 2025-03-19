estrato = int(input("Ingresa tu estrato: "))
edad = int(input("Ingresa tu edad: "))
precio_matricula = int(input("ingresa el precio de tu matricula:"))


if edad > 18 and estrato == 1:
    descuento = 0.20  # 20%
    print("Tu descuento es del 20%")
elif edad <= 18 and estrato == 1:
    descuento = 0.15  # 15%
    print("Tu descuento es del 15%")
elif edad > 18 and estrato == 2:
    descuento = 0.10  # 10%
    print("Tu descuento es del 10%")
elif edad <= 18 and estrato == 2:
    descuento = 0.05  # 5%
    print("Tu descuento es del 5%")
else:
    descuento = 0
    print("No aplicas a descuento")

precio_final = precio_matricula - (precio_matricula * descuento)

print(f"El precio final de la matrícula después del descuento es: {precio_final}")
