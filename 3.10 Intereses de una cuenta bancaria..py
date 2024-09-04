# Ingreso de datos
capital_inicial = float(input("Ingresa el capital inicial (monto depositado): "))
tasa_interes = float(input("Ingresa la tasa de interés anual (en porcentaje, por ejemplo, 5 para 5%): ")) / 100
tiempo = float(input("Ingresa el tiempo en años: "))

# Cálculo del interés simple
interes = capital_inicial * tasa_interes * tiempo

# Resultado
print(f"\nEl interés ganado después de {tiempo} años es: {interes:.2f}")
