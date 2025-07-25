import nutrigest

def mostrar_menu_principal():
    print("\n" + "=" * 50)
    print("\t\t  🍎 NUTRIGEST - CONTROL NUTRICIONAL".upper())
    print("=" * 50)
    print("\n\t1. AGREGAR ALIMENTO")
    print("\t2. MOSTRAR ALIMENTOS REGISTRADOS")
    print("\t3. CALCULAR CALORÍAS TOTALES")
    print("\t4. VER ALIMENTOS MÁS FRECUENTES")
    print("\t5. INGRESAR DATOS PERSONALES")
    print("\t6. SALIR DEL SISTEMA")
    print("\n" + "-" * 50)

def main():
    nutrigest.borrarPantalla()
    print("\n\t\t\t🍎 BIENVENIDO A NUTRIGEST 🍎")
    print("\n\tAntes de comenzar, ingresa tus datos personales.")
    nutrigest.esperarTecla()
    nutrigest.ingresar_datos_usuario()

    while True:
        nutrigest.borrarPantalla()
        mostrar_menu_principal()
        opcion = input("\n\tINGRESE UNA OPCIÓN (1-6): ").strip()

        match opcion:
            case "1":
                nutrigest.agregar_alimento()
            case "2":
                nutrigest.mostrar_alimentos()
            case "3":
                nutrigest.calcular_calorias()
            case "4":
                nutrigest.mostrar_frecuentes()
            case "5":
                nutrigest.ingresar_datos_usuario()
            case "6":
                print("\n\t🚪 Saliendo del sistema... ¡Hasta pronto! 🍏")
                break
            case _:
                print("\n\t❌ ERROR: Opción no válida. Intente nuevamente.")

        nutrigest.esperarTecla()

if __name__ == "__main__":
    main()