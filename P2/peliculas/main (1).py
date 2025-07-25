
'''
Crear un proyecto que permita gestionar (administrar) peliculas
Colocar un menu de opciones para agregar, borrar, modificar, mostrar, buscar, limpiar una lista de peliculas

notas: 
1.- Utilizar funciones y mandar llamar desde otro archivo (modulo)
2.- Utilizar listas para almacenar los los atributos (nombre, categoria, clasificacion, genero, idioma)
'''
import os
os.system("cls")
import peliculas.peliculas as peliculas
opcion = True

while opcion:
    peliculas.borrarPantalla()
    print("\n\t1.- Agregar pelicula \n\t2.- Borrar pelicula \n\t3.- Modificar pelicula \n\t4.- Mostrar peliculas " \
    "\n\t5.- Buscar pelicula \n\t6.- Limpiar lista de peliculas \n\t7.- Salir")
    opcion = input("\n\tSelecciona una opcion: ").upper()

    match opcion:
        case "1":
            peliculas.agregarPelicula()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPelicula()
            peliculas.esperarTecla()
        case "3":
            peliculas.modificarPelicula()
            peliculas.esperarTecla()
        case "4":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
        case "5":
            peliculas.buscarPelicula()
            peliculas.esperarTecla()
        case "6":
            peliculas.limpiarPeliculas()
            peliculas.esperarTecla()
        case "7":
            print("\n\tTerminaste la ejecucion del programa. Gracias por usarlo")
            peliculas.borrarPantalla()
            opcion = False
        case _:
            print("\n\tOpcion no valida, por favor selecciona una opcion del menu")
            peliculas.esperarTecla()
            opcion = True
