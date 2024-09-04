import math

def grados_a_radianes(grados):
    return grados * (math.pi / 180)

def radianes_a_grados(radianes):
    return radianes * (180 / math.pi)

# Menú para seleccionar la conversión
print("Seleccione la conversión:")
print("1. Convertir de grados a radianes")
print("2. Convertir de radianes a grados")
opcion = int(input("Ingrese 1 o 2: "))

if opcion == 1:
    grados = float(input("Ingrese el ángulo en grados: "))
    radianes = grados_a_radianes(grados)
    print(f"{grados} grados son {radianes:.4f} radianes")
elif opcion == 2:
    radianes = float(input("Ingrese el ángulo en radianes: "))
    grados = radianes_a_grados(radianes)
    print(f"{radianes:.4f} radianes son {grados:.2f} grados")
else:
    print("Opción no válida")
