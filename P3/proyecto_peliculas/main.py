'''
Crear un proyecto que permita gestionar (administrar) peliculas. Colocar un menu de opciones: Agregar, Borrar, Modificar, Mostrar, Buscar peliculas.

Notas: 
1.- Utilizar funciones y mandar llamar desde otro archivo (modulo)
2.- Utilizar dict para almacenar los atributos (nombre,categoria,clasificacion,genero,idioma) de peliculas
3.- Implementar y utlizar una BD Relacional en MySQL

'''

import peliculas

opcion=True

while opcion:
   peliculas.borrarPantalla()
   print("\n\t\t\t .::: GESTION DE PELICULAS :::. \n\n\t 1.- Crear \n\t 2.- Borrar \n\t 3.- Mostrar \n\t 4.- Buscar \n\t 5.- Modificar \n\t 6.- Salir")
   opcion=input("\n\t\t Elige una opción: ").upper()

   match opcion:
      case "1":
         peliculas.crearPeliculas()
         peliculas.esperarTecla()
      case "2":
         peliculas.borrarPeliculas()
         peliculas.esperarTecla() 
      case "3":
         peliculas.mostrarPeliculas()
         peliculas.esperarTecla()  
      case "4":
         peliculas.buscarPeliculas()
         peliculas.esperarTecla()
      case "5":
         peliculas.modificarPeliculas()
         peliculas.esperarTecla()
      case "6":
         opcion=False
         peliculas.borrarPantalla()
         print("\n\tTerminaste la ejecución del Sistema ... Gracias ...")
      case _:
         opcion=True
         peliculas.esperarTecla()
         print("\n\tOpción Invalida vuelva a intentarlo")   

                        