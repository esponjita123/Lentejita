# Ingreso del tamaño del cuadrado
tamaño = int(input("Ingresa el tamaño del cuadrado: "))

# Dibujo del cuadrado
for i in range(tamaño):
    if i == 0 or i == tamaño - 1:
        print("*" * tamaño)  # Lado superior e inferior
    else:
        print("*" + " " * (tamaño - 2) + "*")  # Lados izquierdo y derecho
