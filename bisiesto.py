"""
Larisa Carolina Alvarez Gonzalez 763374
"""


# Entradas
year = int(input("Introduzca un año: "))

# Proceso
if (year % 4  == 0 and year % 100 != 0) or (year % 400 == 0):
    salida = str(year) + " sí es un año bisiesto"
else:
    salida = str(year) + " no es un año bisiesto" 
# Salidas
print(salida)
