opcion = 0 
while opcion != 2:
    print("--- MENU TIENDA RETAIL ---")
    print("1. Registrar compra")
    print("2. Salir")
    try:
        opcion = int(input("seleccione una opcion:"))
    except:
        print("error: debe ingresar un numero entero.")
        opcion = 0
    if opcion == 1:
        print("registro de compra")
        monto_valido = False
        while monto_valido == False:
            try:
                monto = int(input("ingrese el mondo de compra: $"))
                if monto > 0:
                    monto_valido = True
                else:
                    print("error: el monto debe ser mayor a cero.")
            except:
                print("error: debe ingresar un nuevo numero entero")

        tipo_cliente = input("ingrese tipo de cliente (premium/socio/normal:)")
        tipo_cliente = tipo_cliente.lower().strip()
        if tipo_cliente == "premium":
             porcentaje = 0.20
        elif tipo_cliente == "socio":
            porcentaje = 0.10
        elif tipo_cliente == "normal":    
            porcentaje = 0
        else:
            porcentaje = 0
            print("tipo de cliente no reconocido. No se aplicara descuento")
        descuento = monto  * porcentaje
        total = monto - descuento
        print("monto original: $", monto) 
        print("descuento aplicado: $", int(descuento))
        print("total a pagar: $", int(total))        
    elif opcion == 2:
        print ("gracias por usar el sistema")
    else:
        print("opcion invalida")
