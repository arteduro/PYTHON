import datetime

# Diccionario que almacena los productos de la PYME
productos = {
    "01": {"nombre": "Producto A", "precio": 1000, "inventario": 100},
    "02": {"nombre": "Producto B", "precio": 2000, "inventario": 50},
    "03": {"nombre": "Producto C", "precio": 3000, "inventario": 200},
    "04": {"nombre": "Producto D", "precio": 4000, "inventario": 75},
    "05": {"nombre": "Producto E", "precio": 5000, "inventario": 150},
}

# Función para mostrar el inventario actual
def mostrar_inventario():
    print("Inventario actual: ")
    for clave, producto in productos.items():
        print(clave, producto["nombre"], producto["inventario"])

# Función para realizar una venta
def vender():
    print("Productos disponibles: ")
    for clave, producto in productos.items():
        print(clave, producto["nombre"], producto["precio"])
    codigo_producto = input("Ingrese el código del producto: ")
    cantidad = int(input("Ingrese la cantidad a vender: "))
    if codigo_producto in productos:
        producto = productos[codigo_producto]
        if producto["inventario"] >= cantidad:
            producto["inventario"] -= cantidad
            ganancia = cantidad * producto["precio"]
            ventas_hoy.append(ganancia)
            print(f"Se vendieron {cantidad} unidades de {producto['nombre']} por un total de {ganancia} pesos")
        else:
            print("No hay suficiente inventario para realizar la venta")
    else:
        print("El código de producto ingresado no es válido")

# Función para mostrar las ventas del día
def ventas_diarias():
    total = sum(ventas_hoy)
    print(f"Las ventas de hoy ({datetime.date.today()}) son de {total} pesos")

# Función para mostrar las ventas del mes
def ventas_mensuales():
    total = sum(ventas_mes)
    print(f"Las ventas del mes ({datetime.date.today().strftime('%B')}) son de {total} pesos")

# Función para actualizar las ventas mensuales
def actualizar_ventas_mes():
    if datetime.date.today().day == 1:
        ventas_mes.append(sum(ventas_hoy))
        ventas_hoy.clear()

# Inicialización de las variables de ventas
ventas_hoy = []
ventas_mes = []

# Ejecución del programa
while True:
    print("Menu: ")
    print("1. Mostrar inventario")
    print("2. Vender producto")
    print("3. Mostrar ventas del día")
    print("4. Mostrar ventas del mes")
    opcion = input("Ingrese la opción deseada: ")
    if opcion == "1":
        mostrar_inventario()
    elif opcion == "2":
        vender()
    elif opcion == "3":
        ventas_diarias()
    elif opcion == "4":
        ventas_mensuales()
    else:
        print("Opción no válida")
    actualizar_ventas_mes()
