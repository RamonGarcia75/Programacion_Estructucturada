import agenda

def main():
    opcion=True

    while opcion:
        opcion = agenda.menu_principal()
        if opcion == "1":
            agenda.agregar_contacto()
            agenda.esperar_Tecla()
        elif opcion == "2":
            agenda.mostrar_contactos()
            agenda.esperar_Tecla()
        elif opcion == "3":
            agenda.buscar_contacto()
            agenda.esperar_Tecla()
        elif opcion == "4":
            agenda.modificar_contacto()
            agenda.esperar_Tecla()
        elif opcion == "5":
            agenda.eliminar_contacto()
            agenda.esperar_Tecla()
        elif opcion == "6":
            agenda.borrarPantalla()
            print("\n\t\t\t\t\t👋 Programa Finalizado")
            opcion = False
        else:
            opcion = False
            print("\n\t\t\t\t\t❌ Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()