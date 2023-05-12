 
# Definir el diccionario de países
paises = {
    "Argentina": {
        "presidente": "Alberto Fernández",
        "moneda": "peso argentino",
        "anio_independencia": 1816,
        "capital": "Buenos Aires"
    },
    "Brasil": {
        "presidente": "Jair Bolsonaro",
        "moneda": "real brasileño",
        "anio_independencia": 1822,
        "capital": "Brasilia"
    },
    "Colombia": {
        "presidente": "Iván Duque",
        "moneda": "peso colombiano",
        "anio_independencia": 1810,
        "capital": "Bogotá"
    },
    "Ecuador": {
        "presidente": "Guillermo Lasso",
        "moneda": "dólar estadounidense",
        "anio_independencia": 1822,
        "capital": "Quito"
    },
    "México": {
        "presidente": "Andrés Manuel López Obrador",
        "moneda": "peso mexicano",
        "anio_independencia": 1810,
        "capital": "Ciudad de México"
    }
}

# Pedir al usuario que ingrese el nombre del país
pais = input("Ingresa el nombre del país de América: ")

# Obtener la información del país del diccionario
informacion = paises.get(pais)

# Mostrar la información al usuario
if informacion:
    print("Presidente actual:", informacion.get("presidente"))
    print("Moneda:", informacion.get("moneda"))
    print("Año de independencia:", informacion.get("anio_independencia"))
    print("Capital:", informacion.get("capital"))
else:
    print("No se encontró información para ese país.")
