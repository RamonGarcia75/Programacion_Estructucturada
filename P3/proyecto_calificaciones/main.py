import os
import calificaciones
os.system('cls')

#NOTAS:
#1.- Utilizar funciones y mandar llamar desde otro archivo(modulos)
#2.- Utilizar list (bidimencional) para almacenar el nombre del alumno, asi como sus tres calificaciones


def main(): 
    while True:
        calificaciones.borrarPantalla()
        opcion = calificaciones.menu_principal()    
        
        match opcion:
            case "1":
                calificaciones.agregarAlumno()  # función conectada a la base
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrarAlumnos()
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcularPromedios()
                calificaciones.esperarTecla()
            case "4":
                calificaciones.buscarAlumno()
                calificaciones.esperarTecla()
            case "5":
                print("\n\t\t🎉 Terminaste la ejecución del programa. ¡Gracias por usarlo!")
                break
            case _:
                print("\n\t\t❌ Opción inválida, vuelve a intentarlo ❌")
                calificaciones.esperarTecla()

if __name__ == "__main__":
    main()