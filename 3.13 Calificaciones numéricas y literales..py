# Ingreso de la calificación numérica
calificacion_numerica = float(input("Ingresa la calificación numérica: "))

# Conversión a calificación literal
if 90 <= calificacion_numerica <= 100:
    calificacion_literal = "A"
elif 80 <= calificacion_numerica < 90:
    calificacion_literal = "B"
elif 70 <= calificacion_numerica < 80:
    calificacion_literal = "C"
elif 60 <= calificacion_numerica < 70:
    calificacion_literal = "D"
elif 0 <= calificacion_numerica < 60:
    calificacion_literal = "F"
else:
    calificacion_literal = "Calificación inválida"

# Resultado
print(f"La calificación literal es: {calificacion_literal}")
