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
    modelo = input("Ingresá el modelo del vehículo: ")
    año = input("Ingresá el año del vehículo: ")
    patente = input("Ingresá la patente del vehículo: ")
    precio = input("Ingresá el precio por día del vehículo: ")

    # para verificar que no exista la patente y se agregue un auto con una duplicada. pregunta si la variable "patente" existe en el array patentes, después habría que hacer que cuando ingrese una patente repetida, se la pída de vuelta, así no tiene que completar todos los datos de nuevo (SEMANA 5)
    # if patente in patentes:
    #     print("Ya existe un auto con esa patente. Volvé a intentarlo")
    #     return

    #para verificar si la pantente que se quiere registrar ya existe
    repetido = False
    for i in range(len(patentes)):
        if patentes[i] == patente:
            repetido = True
    
    if repetido == True:
        print("Error: la patente ya está registrada")
        print("No se pudo registrar el auto")
    else:
        # si no está repetida, agregamos los datos que ingresó ewl usuario a las listas paralelas
        marcas.append(marca)
        modelos.append(modelo)
        años.append(año)
        patentes.append(patente)
        precios.append(precio)
        estados.append("Disponible")
        print("Auto registrado correctamente: ", marca, modelo, "(", patente , ")")

# aca vamos a agregar todas las funcionalidades del usuario, por ahora ver autos y regitrar uno, depués "alquilar auto" por ejemplo. comienza cargando los autos precargados
def menu():
    cargarAutosExistentes()
    while True:
        print("--- MENÚ PRINCIPAL DRIVIO ---")
        print("1. Mostrar autos")
        print("2. Registrar nuevo auto")
        print("3. Salir")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            mostrarAutos()
        elif opcion == "2":
            registrarAuto()
        elif opcion == "3":
            print("GRACIAS POR USAR DRIVIO")
            break
        else:
            print("Opción inválida. Intentá de nuevo.")


menu()