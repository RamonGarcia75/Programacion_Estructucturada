from gestor import registrar_usuario, agregar_alimento, generar_reporte, borrar_pantalla, esperar_tecla
from exportaciones import exportar_a_pdf, exportar_a_excel

def mostrar_menu():
    print("\n" + "="*50)
    print(" NUTRIGEST - SISTEMA DE GESTIÓN NUTRICIONAL ".center(50))
    print("="*50)
    print("\n1. Registrar nuevo usuario")
    print("2. Registrar consumo de alimento")
    print("3. Generar reporte diario")
    print("4. Exportar datos a PDF")
    print("5. Exportar datos a Excel")
    print("6. Salir")
    print("\n" + "="*50)

def main():
    while True:
        borrar_pantalla()
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-6): ").strip()
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            agregar_alimento()
        elif opcion == "3":
            generar_reporte()
        elif opcion == "4":
            usuario_id = input("\nIngrese el ID del usuario a exportar: ")
            exportar_a_pdf(usuario_id)
            esperar_tecla()
        elif opcion == "5":
            usuario_id = input("\nIngrese el ID del usuario a exportar: ")
            exportar_a_excel(usuario_id)
            esperar_tecla()
        elif opcion == "6":
            borrar_pantalla()
            print("\n¡Gracias por usar NutriGest! Hasta pronto!\n")
            break
        else:
            print("\n❌ Opción no válida. Por favor ingrese un número del 1 al 6.")
            esperar_tecla()

if __name__ == "__main__":
    main()
