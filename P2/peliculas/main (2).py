
'''
Crear un proyecto que permita gestionar (administrar) peliculas
Colocar un menu de opciones para agregar, borrar, modificar, mostrar, buscar, limpiar una lista de peliculas

notas: 
1.- Utilizar funciones y mandar llamar desde otro archivo (modulo)
2.- Utilizar listas para almacenar los los atributos (nombre, categoria, clasificacion, genero, idioma)
'''
import peliculas.peliculas as peliculas

opcion = True

while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t .:::GESTION DE PELICULAS:::.\n\t1.-crear \n\t2.-Borrar \n\t3.-Mostrar" \
    "\n\t4.-Agreagar una caracteristica\n\t5.-modificar caracteristica\n\t6.-Borrar Caracteristica\n\t7.-Salir del Sistema")
    opcion = input("\n\t\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.esperarTecla()

        case "2":
            peliculas.borrarPeliculas()
            peliculas.esperarTecla()

        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()

        case "4":
            peliculas.agregarCaracteristicaPeliculas()
            peliculas.esperarTecla()

        case "5":
            peliculas.modificarCaracteristicaPeliculas()
            peliculas.esperarTecla()

        case "6":
            peliculas.borrarCaracteristicaPeliculas()
            peliculas.esperarTecla()

        case "7":
            opcion = False
            peliculas.borrarPantalla()
            print("\n\tTerminaste la ejecución del Sistema...Gracias")

        case _:
            print("\n\tOpción Inválida, vuelva a intentarlo")
            peliculas.esperarTecla()

