peliculas = []

def borrarPantalla():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def esperarTecla():
    input("\nPresiona una tecla para continuar...")

def agregarPelicula():
    borrarPantalla()
    print("\n\t::Agregar Peliculas::\n")
    pelicula = input("Ingrese el nombre: ").upper().strip()
    peliculas.append(pelicula)
    print("\n\tLa operación se realizó con éxito")

def mostrarPeliculas():
    borrarPantalla()
    print("::Mostrar todas las Peliculas::")
    if len(peliculas) > 0:
        for i in range(0, len(peliculas)):
            print(f"{i+1} : {peliculas[i]}")
    else:
        print("No hay películas en este momento en el sistema")

def limpiarPeliculas():
    borrarPantalla()
    print("::Limpiar todas las Peliculas::")
    resp = input("¿Deseas borrar todas las películas del sistema? (SI/NO): ").lower().strip()
    if resp == "si":
        peliculas.clear()
        print("\n\tLa operación se realizó con éxito")

def buscarPelicula():
    borrarPantalla()
    print("::Buscar Peliculas::")
    pelicula_buscar = input("Ingrese el nombre de la película a buscar: ").upper().strip()
    
    if pelicula_buscar not in peliculas:
        print("\n\t:::Esta película no existe en el sistema:::")
    else:
        encontradas = 0
        for i in range(0, len(peliculas)):
            if pelicula_buscar == peliculas[i]:
                print(f"\n\tLa película '{pelicula_buscar}' se encontró en la posición {i+1}")
                encontradas += 1
        print(f"\nTenemos {encontradas} película(s) con este título")

def modificarPelicula():
    borrarPantalla()
    print("::Modificar Peliculas::")
    pelicula_buscar = input("Ingrese el nombre de la película a modificar: ").upper().strip()
    
    if pelicula_buscar not in peliculas:
        print("\n\t:::Esta película no existe en el sistema:::")
    else:
        modificadas = 0
        for i in range(0, len(peliculas)):
            if pelicula_buscar == peliculas[i]:
                resp = input("¿Deseas actualizar esta película? (SI/NO): ").lower()
                if resp == "si":
                    nuevo_nombre = input("\nIntroduce el nuevo nombre: ").upper().strip()
                    peliculas[i] = nuevo_nombre
                    modificadas += 1
        print(f"\nSe modificó {modificadas} película(s)")