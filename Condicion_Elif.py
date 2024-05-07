'''

si la edad es menor a 16, no puede conducir
si la edad es menor a 18 puede obtener permiso para conducir.
si la edad es menor  a 70,puede obtener permiso estandar.
si la edad es mayor a 70, necesita un permiso especial

'''

edad = int(input("Ingrese su edad: "))


if edad<16:
            print("No puede conducir")
elif edad>=16 and edad<18:
    print("Puede obtar por una licencia")

elif edad>=18 and edad<=70:
        print("puede obtener permiso estandar")
elif  edad>70:
    print("necesita un permiso especial de conduccion")
else:
        print("no puede conducir")
