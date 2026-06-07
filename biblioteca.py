print("¡Bienvenid@ al sistema de gestion de prestamos de la biblioteca central!")

libros = 120
prestamos = 0
while True:
    print("\n=== MENU PRINCIPAL === ")
    print("1. Libros disponibles")
    print("2. Realizar prestamos")
    print("3. Devolver prestamo")
    print("4. Historial de prestamos")
    print("5. Salir")
    opcion = input("Seleccione una opcion:")

    if opcion == "1":
        print("Libros disponibles:", libros)
    elif opcion == "2":
        cantidad = int(input("¿Cuantos libros desea pedir?:"))
        if cantidad > 0 and cantidad <= libros:
            libros -= cantidad
            prestamos += cantidad
            print("Prestamo realizado correctamente")
        else:
            print("Cantidad invalida o no hay suficientes libros ")

    elif opcion == "3":
        cantidad = int(input("¿Cuantos libros devuelve?: "))
        if cantidad > 0 and prestamos >= cantidad:
            libros += cantidad
            prestamos -= cantidad
            print("Devolucion realizada")
        else:
            print("Cantidad invalida")
    elif opcion == "4":
        print("Prestamos activos:", prestamos)
    elif opcion == "5":
        print("Gracias por utilizar nuestro software, hasta la proxima.")
        break
    else:
        print("Opcion invalida")                        
