# creo las listas paralelas para después rellenarlas con los datos de los autos que vamos a precargar
marcas = []
modelos = []
patentes = []
años = []
precios = []
estados = []

def cargarAutosExistentes():
    # creo la lista autos con los datos necesarios
    autos = [
        ["Toyota", "Corolla", "ABC123", 2020, 25000, "Disponible"],
        ["Ford", "Fiesta", "DEF456", 2019, 20000, "Disponible"],
        ["Chevrolet", "Onix", "GHI789", 2021, 27000, "Disponible"],
        ["Volkswagen", "Gol", "JKL321", 2018, 18000, "Disponible"],
        ["Peugeot", "208", "MNO654", 2022, 30000, "Disponible"],
        ["Renault", "Clio", "PQR987", 2017, 16000, "Disponible"],
        ["Chevrolet", "Cruze", "QRS753", 2023, 34000, "Disponible"],
        ["Fiat", "Cronos", "STU147", 2023, 32000, "Disponible"],
        ["Nissan", "Versa", "VWX258", 2021, 29000, "Disponible"],
        ["Honda", "Civic", "EFG852", 2022, 35000, "Disponible"],
        ["Toyota", "Yaris", "HIJ963", 2018, 21000, "Disponible"],
        ["Ford", "Focus", "KLM159", 2021, 28000, "Disponible"],
        ["Volkswagen", "Polo", "NOP357", 2020, 27500, "Disponible"]
    ]

    # creo un bucle para agregar a las listas paralelas todos los datos correspondientes, por ejemplo a la lista marcas, le agrego de cada auto, la posicion 0
    for auto in autos:
        marcas.append(auto[0])
        modelos.append(auto[1])
        patentes.append(auto[2])
        años.append(auto[3])
        precios.append(auto[4])
        estados.append(auto[5])



# creo la funcion para mostrar los autos, por ahora muestra todos, después tendríamos que hacer una que muestre solo los disponibles
def mostrarAutos():
    print("----- AUTOS EN 'DRIVIO' -----")
    # bucle para recorrer todos los autos, uso length de marcas pero se puede usar cualquiera porque tienen todos el mismo largo
    for i in range(len(marcas)):
        print(i+1, ". ", marcas[i], modelos[i], años[i], " - Patente: ", patentes[i], " - $", precios[i], " por día - Estado: ", estados[i])

# funcion para evitar que se carguen autos duplicados
# def insertarUnico(lista, dato):
#     for i in range(len(lista)):
#         if lista[i] == dato:
#             print("Error: la patente ya está registrada")
#             return False
#     lista.append(dato)
#     print("Auto agregado correctamente")
#     return True

def registrarAuto():
    print("----- REGISTRAR AUTO -----")
    # pongo todos los campos que necesitamos para crear un nuevo auto, después hay que validar los datos ingresados (SEMANA 5). No ponemos el estado ya que después lo creamos con "Disponible"
    marca = input("Ingresá la marca del vehículo: ")
    while len(marca) < 1:
        print("Ingrese una marca válida.")
        marca = input("Ingresá la marca del vehículo: ")

    modelo = input("Ingresá el modelo del vehículo: ")
    while len(modelo) < 1:
        print("Ingrese un modelo válida.")
        modelo = input("Ingresá el modelo del vehículo: ")

    año = int(input("Ingresá el año del vehículo: "))
    while año < 2010 or año > 2025:
        print("Ingrese un año mayor a 2010 y menor a 2025.")
        año = int(input("Ingresá el año del vehículo: "))

    # la validacion de la patente la movemos para acá, para que si la patente ya existe, no tenga que volver a ingresar todos los datos   
    patente_valida = False
    while not patente_valida:
        patente = input("Ingresá la patente del vehículo: ")

        # verificamos que tenga el largo correcto
        if len(patente) < 5 or len(patente) > 7 or patente.isalnum() == False:
            print("La patente debe tener entre 5 y 7 caracteres y solo letras o números.")
            continue

        # verificar si la patente ya existe
        repetida = False
        for i in range(len(patentes)):
            if patentes[i] == patente:
                repetida = True

        if repetida:
            print("La patente ya está registrada.")
        else:
            patente_valida = True
    
    precio = int(input("Ingresá el precio por día del vehículo: "))
    while precio < 1000 or precio > 100000:
        print("Ingrese un precio entre 1.000 y 100.000.")
        precio = int(input("Ingresá el precio por día del vehículo: "))

    # para verificar que no exista la patente y se agregue un auto con una duplicada. pregunta si la variable "patente" existe en el array patentes, después habría que hacer que cuando ingrese una patente repetida, se la pída de vuelta, así no tiene que completar todos los datos de nuevo (SEMANA 5)
    # if patente in patentes:
    #     print("Ya existe un auto con esa patente. Volvé a intentarlo")
    #     return

    #para verificar si la pantente que se quiere registrar ya existe
    # repetido = False
    # for i in range(len(patentes)):
    #     if patentes[i] == patente:
    #         repetido = True
    
    # if repetido == True:
    #     print("Error: la patente ya está registrada")
    #     print("No se pudo registrar el auto")

        # si no está repetida, agregamos los datos que ingresó ewl usuario a las listas paralelas
        marcas.append(marca)
        modelos.append(modelo)
        años.append(año)
        patentes.append(patente)
        precios.append(precio)
        estados.append("Disponible")
        print("Auto registrado correctamente: ", marca, modelo, "(", patente , ")")


def alquilarAuto():
    # mostramos el auto a alquilar y despues dejamos que el usuario elija el que desee
    mostrarAutos()
    print("----- ALQUILAR AUTO -----")
    autoSeleccionado = int(input(f"Seleccioná el auto a alquilar (1 - {len(patentes)}): "))
    while autoSeleccionado < 1 or autoSeleccionado > len(patentes):
        print(f"Ingresa un número dentro del rango. 1 - {len(patentes)}")
        autoSeleccionado = int(input(f"Seleccioná nuevamente (1 - {len(patentes)}): "))

    indice = autoSeleccionado - 1

    if indice < 0 or indice >= len(patentes):
        print("Número invalido")
        return
    
    # verificamos que el auto que seleccionó el usuario no este alquildo
    if estados[indice] == "Alquilado":
        print("El auto ", marcas[indice], modelos[indice], "(", patentes[indice], ") ya está alquilado")
        return
    
    print("Seleccionaste: ", marcas[indice], modelos[indice], "(", patentes[indice], ")")

    # diasSeleccionados = int(input("Seleccioná la cantidad de días que lo queres alquilar: "))

    # if diasSeleccionados < 1:
    #     print("Debés alquilarlo al menos por un día")
    #     return

    diasSeleccionados = int(input("¿Por cuántos días querés alquilarlo?: "))
    while diasSeleccionados < 1:
        print("Debes alquilarlo al menos por un día.")
        diasSeleccionados = int(input("¿Por cuántos días querés alquilarlo?: "))

    
    total = diasSeleccionados * precios[indice]

    print("El total a pagar es de: $", total)
    confirma = int(input(f"¿Deseás alquilar {marcas[indice]} {modelos[indice]} ({patentes[indice]}) por {diasSeleccionados} días y ${total}? (1 = SI, 2 = NO): "))
    while confirma < 1 or confirma > 2:
        print("Ingresá 1 para SI o 2 para NO.")
        confirma = int(input(f"¿Deseás alquilar {marcas[indice]} {modelos[indice]} ({patentes[indice]}) por {diasSeleccionados} días y ${total}? (1 = SI, 2 = NO): "))



    if confirma == 1:
        estados[indice] = "Alquilado"
        print("Alquiler confirmado de: ", marcas[indice], modelos[indice], "(", patentes[indice], ")")
        print("Debés abonar: $", total)
    elif confirma == 2:
        print("Alquiler cancelado. El auto sigue disponible")

# funcion para que el usuario pueda ordenar de mayor a menor o al reves los precios de los autos, y despues guarda los datos en los respectivos arrays
def burbujeoOrden(ascendente=True):
    n = len(precios)
    for i in range(n):
        for j in range(0, n - i - 1):
            # comparo segun el tipo de ordenamiento
            if (ascendente and precios[j] > precios[j + 1]) or (not ascendente and precios[j] < precios[j + 1]):
                # intercambio los precios
                precios[j], precios[j + 1] = precios[j + 1], precios[j]
                # intercambio también las otras listas para mantener consistencia
                marcas[j], marcas[j + 1] = marcas[j + 1], marcas[j]
                modelos[j], modelos[j + 1] = modelos[j + 1], modelos[j]
                patentes[j], patentes[j + 1] = patentes[j + 1], patentes[j]
                años[j], años[j + 1] = años[j + 1], años[j]
                estados[j], estados[j + 1] = estados[j + 1], estados[j]


# Funcion para que el usuario elija como filtrar por precip, usa burbujeoOrden
def filtrarPorPrecio():
    print("----- FILTRAR AUTOS POR PRECIO -----")
    print("1. De menor a mayor")
    print("2. De mayor a menor")

    opcion = int(input("Elegí una opción: "))
    while opcion < 1 or opcion > 2:
        print("Debés ingresar 1 o 2.")
        opcion = int(input("Elegí una opción (1 = menor a mayor / 2 = mayor a menor): "))

    if opcion == 1:
        burbujeoOrden(ascendente=True)
        print("Autos ordenados de menor a mayor precio:")
        mostrarAutos()
    elif opcion == 2:
        burbujeoOrden(ascendente=False)
        print("Autos ordenados de mayor a menor precio:")
        mostrarAutos()
    else:
        print("Opción inválida.")

# aca vamos a agregar todas las funcionalidades del usuario, por ahora ver autos y regitrar uno, depués "alquilar auto" por ejemplo. comienza cargando los autos precargados
def menu():
    cargarAutosExistentes()
    while True:
        print("--- MENÚ PRINCIPAL DRIVIO ---")
        print("1. Mostrar autos")
        print("2. Registrar nuevo auto")
        print("3. Alquilar auto")
        print("4. Filtrar autos por precio")
        print("5. Salir")

        opcion = int(input("Elegí una opción: "))
        while opcion < 1 or opcion > 5:
            print("Debés ingresar un número entre 1 y 2.")
            opcion = int(input("Elegí una opción: "))

        if opcion == 1:
            mostrarAutos()
        elif opcion == 2:
            registrarAuto()
        elif opcion == 3:
            alquilarAuto()
        elif opcion == 4:
            filtrarPorPrecio()
        elif opcion == 5:
            print("GRACIAS POR USAR DRIVIO")
            break
        else:
            print("Opción inválida. Intentá de nuevo.")


menu()