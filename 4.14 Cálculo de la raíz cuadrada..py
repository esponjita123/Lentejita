import math

# Ingreso de datos
numero = float(input("Ingresa un número para calcular su raíz cuadrada: "))

# Cálculo de la raíz cuadrada
if numero >= 0:
    raiz_cuadrada = math.sqrt(numero)
    print(f"La raíz cuadrada de {numero} es {raiz_cuadrada:.4f}")
else:
    print("No se puede calcular la raíz cuadrada de un número negativo en el conjunto de los números reales.")
