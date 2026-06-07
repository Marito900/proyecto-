print("=== Hospital Central Metropolitano ===")

especialistas = 0 
residentes = 0 
while True:
    try:
        cantidad = int(input("¿Cuantos medicos desea registrar?: "))
        if cantidad > 0:
            break
        else:
            print("¡Registro medicos invalido! Ingresa un entero positivo para continuar.")
    except:
        print("¡Registro medico invalido! Ingresa un entero positivo para continuar.")

for i in range(cantidad):
    print(f"\nRegistro medico {i + 1}")
    while True:
        nombre = input("Nombre del Profesional: ")
        if len (nombre) >= 6 and " " not in nombre:
            break
        else:
            print("Nombre invalido. Debe tener minimo 6 caracteres y sin espacios.")
while True:
    try:
        experiencia = int(input("Años de experiencia:" ))
        if experiencia >= 0:
            break
        else:
            print("¡ERROR CLINICO! Ingresa un numero entero positivo para la experiencia.")
    except:
        print("¡ERROR CLINICO! Ingresa un numero entero positivo para la experiencia.")  

if experiencia > 5:
    especialistas += 1
    print(nombre, "Especialista Senior")
else:
    residentes += 1
    print(nombre, "Residente junior")


print("\n=== Resumen final ===")

print(
"El Hospital cuenta con", 
especialistas,
"Especialistas Senior y",
residentes,
"¡Residentes Junior! ¡Sistema listo para operar! "
)   
    



        