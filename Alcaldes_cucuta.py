 
alcaldes = {
    1988: "Margarita Silva de Uribe",
    1989: "Margarita Silva de Uribe",
    1990: "Jairo Slebi Medina",
    1991: "Jairo Slebi Medina",
    1992: "Enrique Cuadros Corredor",
    1993: "Enrique Cuadros Corredor",
    1994: "Enrique Cuadros Corredor",
    1995: "Pauselino Camargo",
    1996: "Pauselino Camargo",
    1997: "Pauselino Camargo",
    1998: "José Gélvez Albarracín",
    1999: "José Gélvez Albarracín",
    2000: "José Fernando Bautista",
    2001: "Manuel Guillermo Mora",
    2002: "Manuel Guillermo Mora",
    2003: "Manuel Guillermo Mora",
    2004: "Ramiro Suárez Corzo",
    2005: "Ramiro Suárez Corzo",
    2006: "Ramiro Suárez Corzo",
    2007: "Ramiro Suárez Corzo",
    2008: "María Eugenia Riascos",
    2009: "María Eugenia Riascos",
    2010: "María Eugenia Riascos",
    2011: "María Eugenia Riascos",
    2012: "Donamaris Ramírez-Paris Lobo",
    2013: "Donamaris Ramírez-Paris Lobo",
    2014: "Donamaris Ramírez-Paris Lobo",
    2015: "Donamaris Ramírez-Paris Lobo",
    2016: "César Rojas Ayala",
    2017: "César Rojas Ayala",
    2018: "César Rojas Ayala",
    2019: "César Rojas Ayala",
    2020: "Jairo Yáñez Rodríguez",
    2021: "Jairo Yáñez Rodríguez",
    2022: "Jairo Yáñez Rodríguez",
    2023: "Jairo Yáñez Rodríguez",
}

while True:
    try:
        year = int(input("Ingrese el año para consultar al alcalde de Cúcuta: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número entero.")

if year in alcaldes:
    print(f"El alcalde de Cúcuta para el año {year} fue {alcaldes[year]}.")
else:
    print("No se encontró información del alcalde para el año ingresado.")
