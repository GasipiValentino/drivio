# creo las listas paralelas para después rellenarlas con los datos de los autos que vamos a precargar
marcas = []
modelos = []
patentes = []
años = []
precios = []
estados = []

# listas par. necesarias para mostrar el alquiler de los autos
historial_autos = []
historial_dias = []
historial_montos = []

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

        # Guardar los datos del auto que alquiló el usuaroi para despues poder mostrarlo correctamente en el historial
        autoAlquilado = marcas[indice] + " " + modelos[indice]
        historial_autos.append(autoAlquilado)
        historial_dias.append(diasSeleccionados)
        historial_montos.append(total)
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


# funcion para que el usuario elija como filtrar por precip, usa burbujeoOrden
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

def devolverAuto():
    print("\n----- DEVOLVER AUTO -----")
    
    hayAlquilados = False
    for i in range(len(estados)):
        if estados[i] == "Alquilado":
            hayAlquilados = True
            break
    
    if not hayAlquilados:
        print("No hay autos alquilados para devolver.\n")
        return
    
    print("Autos alquilados:")
    autosAlquilados = []
    for i in range(len(estados)):
        if estados[i] == "Alquilado":
            autosAlquilados.append(i)
            print(len(autosAlquilados), ". ", marcas[i], modelos[i], " - Patente: ", patentes[i])
    
    seleccion = int(input(f"Seleccioná el auto a devolver (1 - {len(autosAlquilados)}): "))
    while seleccion < 1 or seleccion > len(autosAlquilados):
        print(f"Ingresa un número dentro del rango. 1 - {len(autosAlquilados)}")
        seleccion = int(input(f"Seleccioná nuevamente (1 - {len(autosAlquilados)}): "))
    
    indice = autosAlquilados[seleccion - 1]
    estados[indice] = "Disponible"
    print("Auto devuelto correctamente: ", marcas[indice], modelos[indice], "(", patentes[indice], ")")
    print("El auto ahora está disponible para alquilar.\n")

# funcioon para mostrar el historiakl de autos alquilados y sus respectivos datos (auto dias y monto)
def mostrarHistorial():
    print("\n----- HISTORIAL DE ALQUILERES -----")
    
    if len(historial_autos) == 0:
        print("No hay alquileres registrados aún.\n")
        return
    
    for i in range(len(historial_autos)):
        print(i+1, ". ", historial_autos[i], " - Días: ", historial_dias[i], " - Monto: $", historial_montos[i])
    print()


# funcion para mostrar las estadisticas del sistrma (mostramos estadisitiacs generales como el auto mas viejo/nuevo caro/barato etc y estadisticas de los alquileres)
def mostrarEstadisticas():
    print("\n----- ESTADÍSTICAS DE DRIVIO -----")
    
    totalAutos = len(marcas)
    print("Total de autos en el sistema:", totalAutos)
    
    autosDisponibles = 0
    autosAlquilados = 0
    for i in range(len(estados)):
        if estados[i] == "Disponible":
            autosDisponibles = autosDisponibles + 1
        elif estados[i] == "Alquilado":
            autosAlquilados = autosAlquilados + 1
    
    print("Autos disponibles:", autosDisponibles)
    print("Autos alquilados:", autosAlquilados)
    
    if len(precios) > 0:
        indiceMasCaro = 0
        precioMasCaro = precios[0]
        for i in range(len(precios)):
            if precios[i] > precioMasCaro:
                precioMasCaro = precios[i]
                indiceMasCaro = i
        
        print("Auto más caro:", marcas[indiceMasCaro], modelos[indiceMasCaro], "- $", precioMasCaro, "por día")
    
    if len(precios) > 0:
        indiceMasBarato = 0
        precioMasBarato = precios[0]
        for i in range(len(precios)):
            if precios[i] < precioMasBarato:
                precioMasBarato = precios[i]
                indiceMasBarato = i
        
        print("Auto más barato:", marcas[indiceMasBarato], modelos[indiceMasBarato], "- $", precioMasBarato, "por día")
    
    if len(años) > 0:
        indiceMasNuevo = 0
        añoMasNuevo = años[0]
        for i in range(len(años)):
            if años[i] > añoMasNuevo:
                añoMasNuevo = años[i]
                indiceMasNuevo = i
        
        print("Auto más nuevo:", marcas[indiceMasNuevo], modelos[indiceMasNuevo], "(", añoMasNuevo, ")")
    
    if len(años) > 0:
        indiceMasViejo = 0
        añoMasViejo = años[0]
        for i in range(len(años)):
            if años[i] < añoMasViejo:
                añoMasViejo = años[i]
                indiceMasViejo = i
        
        print("Auto más viejo:", marcas[indiceMasViejo], modelos[indiceMasViejo], "(", añoMasViejo, ")")
    
    if len(precios) > 0:
        sumaPrecios = 0
        for i in range(len(precios)):
            sumaPrecios = sumaPrecios + precios[i]
        
        promedio = sumaPrecios / len(precios)
        print("Precio promedio de alquiler por día: $", int(promedio))
    
    print("\n--- Estadísticas de alquileres ---")
    print("Total de alquileres realizados:", len(historial_autos))
    
    if len(historial_montos) > 0:
        totalRecaudado = 0
        for i in range(len(historial_montos)):
            totalRecaudado = totalRecaudado + historial_montos[i]
        
        print("Total recaudado: $", totalRecaudado)
        
        promedioMonto = totalRecaudado / len(historial_montos)
        print("Monto promedio por alquiler: $", int(promedioMonto))
    
    if len(historial_dias) > 0:
        totalDias = 0
        for i in range(len(historial_dias)):
            totalDias = totalDias + historial_dias[i]
        
        promedioDias = totalDias / len(historial_dias)
        print("Promedio de días por alquiler:", int(promedioDias))
    
    print()

# aca vamos a agregar todas las funcionalidades del usuario, por ahora ver autos y regitrar uno, depués "alquilar auto" por ejemplo. comienza cargando los autos precargados
def menu():
    cargarAutosExistentes()
    while True:
        print("========== MENÚ PRINCIPAL DRIVIO ==========")
        print("1. Mostrar autos disponibles")
        print("2. Alquilar un auto")
        print("3. Registrar un nuevo auto")
        print("4. Filtrar vehículo por precio")
        print("5. Mostrar historial de alquileres")
        print("6. Ver estadísticas de 'Drivio'")
        print("7. Devolver un auto")
        print("8. Salir")
        print("===========================================")

        opcion = int(input("Elegí una opción: "))
        while opcion < 1 or opcion > 8:
            print("Debés ingresar un número entre 1 y 8.")
            opcion = int(input("Elegí una opción: "))

        if opcion == 1:
            mostrarAutos()
        elif opcion == 2:
            alquilarAuto()
        elif opcion == 3:
            registrarAuto()
        elif opcion == 4:
            filtrarPorPrecio()
        elif opcion == 5:
            mostrarHistorial()
        elif opcion == 6:
            mostrarEstadisticas()
        elif opcion == 7:
            devolverAuto()
        elif opcion == 8:
            print("\n¡GRACIAS POR USAR DRIVIO!")
            break


menu()