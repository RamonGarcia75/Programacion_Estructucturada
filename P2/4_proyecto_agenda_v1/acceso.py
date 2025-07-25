# programa sencillo de validacion de edad

# pedimos al usuario su edad 
try:
    edad_usuario = int(input("Por favor, ingresa tu edad: "))

    if edad_usuario >= 18:
        print("Acceso permitido. Eres mayor de edad.")
    else:
        print("Acceso denegado. Eres menor de edad.")

except ValueError:
    print("Por favor, ingresa un número válido.")