# Pedimos el primer número al usuario
# Usamos float() para que el programa acepte decimales
numero1 = float(input("Introduce el primer número: "))

# Pedimos el segundo número
numero2 = float(input("Introduce el segundo número: "))

# Realizamos la operación de suma
resultado = numero1 + numero2

# Mostramos el resultado final
# Usamos f-strings (la 'f' antes de las comillas) para insertar variables fácilmente
print(f"La suma de {numero1} y {numero2} es: {resultado}")