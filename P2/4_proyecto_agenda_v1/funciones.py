# Función para pedir datos al usuario
def pedir_datos():
    nombre = input("Escribe tu nombre: ")
    edad = int(input("Escribe tu edad: "))
    return nombre, edad

# Función para verificar si tiene acceso
def verificar_edad(nombre, edad):
    if edad >= 18:
        print(f"Hola {nombre}, acceso permitido.")
    else:
        print(f"Hola {nombre}, acceso denegado.")

# Programa principal
nombre_usuario, edad_usuario = pedir_datos()
verificar_edad(nombre_usuario, edad_usuario)