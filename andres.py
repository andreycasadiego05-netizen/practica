# Entrada de datos
factura = float(input("Total de la factura: "))
propina = int(input("Porcentaje de propina (10, 12, 15): "))
personas = int(input("Número de personas: "))

# Cálculos
total_con_propina = factura * (1 + propina / 100)
pago_individual = total_con_propina / personas

# Resultado
print(f"Cada persona debe pagar: ${pago_individual:.2f}")