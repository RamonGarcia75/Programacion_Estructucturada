listaPeliculas = []

def borrarPantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\nPresiona ENTER para continuar...")

def agregarPeliculas():
    pelicula = {}
    pelicula['nombre'] = input("Ingresa el nombre de la película: ")
    pelicula['categoria'] = input("Ingresa la categoría de la película: ")
    pelicula['clasificacion'] = input("Ingresa la clasificación de la película: ")
    pelicula['genero'] = input("Ingresa el género de la película: ")
    pelicula['idioma'] = input("Ingresa el idioma de la película: ")
    listaPeliculas.append(pelicula)
    print(f"{pelicula['nombre']} fue agregada a la lista de películas.")

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t\t\t .:::MOSTRAR PELICULAS:::.")
    if not listaPeliculas:
        print("No hay películas para mostrar.")
        return
    for i, pelicula in enumerate(listaPeliculas, start=1):
        print(f"{i}. Nombre: {pelicula['nombre']}")
        print(f"   Categoría: {pelicula['categoria']}")
        print(f"   Clasificación: {pelicula['clasificacion']}")
        print(f"   Género: {pelicula['genero']}")
        print(f"   Idioma: {pelicula['idioma']}")
        print("-" * 40)

def borrarPeliculas():
    borrarPantalla()
    print("\n\t\t\t .:::BORRAR PELICULA:::.")
    if not listaPeliculas:
        print("No hay películas para borrar.")
        return
    
    mostrarPeliculas()
    try:
        idx = int(input("\nIngresa el número de la película a borrar: ")) - 1
        if 0 <= idx < len(listaPeliculas):
            borrada = listaPeliculas.pop(idx)
            print(f"\n{borrada['nombre']} fue eliminada con éxito.")
        else:
            print("\nÍndice fuera de rango.")
    except ValueError:
        print("\nEntrada inválida. Debe ser un número.")

def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t\t\t .:::MODIFICAR PELICULA:::.")
    if not listaPeliculas:
        print("No hay películas para modificar.")
        return

    mostrarPeliculas()
    try:
        idx = int(input("\nIngresa el número de la película a modificar: ")) - 1
        if 0 <= idx < len(listaPeliculas):
            pelicula = listaPeliculas[idx]
            print(f"\nEditando: {pelicula['nombre']}")
            pelicula['nombre'] = input("Nuevo nombre: ") or pelicula['nombre']
            pelicula['categoria'] = input("Nueva categoría: ") or pelicula['categoria']
            pelicula['clasificacion'] = input("Nueva clasificación: ") or pelicula['clasificacion']
            pelicula['genero'] = input("Nuevo género: ") or pelicula['genero']
            pelicula['idioma'] = input("Nuevo idioma: ") or pelicula['idioma']
            print(f"\n{pelicula['nombre']} fue modificada con éxito.")
        else:
            print("\nÍndice fuera de rango.")
    except ValueError:
        print("\nEntrada inválida. Debe ser un número.")

def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t\t\t .:::AGREGAR CARACTERISTICA PELICULA:::.")
    if not listaPeliculas:
        print("No hay películas para agregar características.")
        return

    mostrarPeliculas()
    try:
        idx = int(input("\nIngresa el número de la película: ")) - 1
        if 0 <= idx < len(listaPeliculas):
            pelicula = listaPeliculas[idx]
            if 'caracteristicas' not in pelicula:
                pelicula['caracteristicas'] = []
            nueva_car = input("\nIngresa la característica a agregar: ")
            pelicula['caracteristicas'].append(nueva_car)
            print(f"\nCaracterística agregada a {pelicula['nombre']}.")
        else:
            print("\nÍndice fuera de rango.")
    except ValueError:
        print("\nEntrada inválida. Debe ser un número.")

def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t\t\t .:::BORRAR CARACTERISTICA PELICULA:::.")
    if not listaPeliculas:
        print("No hay películas disponibles.")
        return

    mostrarPeliculas()
    try:
        idx_peli = int(input("\nIngresa el número de la película: ")) - 1
        if 0 <= idx_peli < len(listaPeliculas):
            pelicula = listaPeliculas[idx_peli]
            if 'caracteristicas' not in pelicula or not pelicula['caracteristicas']:
                print("\nEsta película no tiene características.")
                return
                
            print(f"\nCaracterísticas de {pelicula['nombre']}:")
            for i, car in enumerate(pelicula['caracteristicas'], 1):
                print(f"{i}. {car}")
                
            idx_car = int(input("\nIngresa el número de la característica a borrar: ")) - 1
            if 0 <= idx_car < len(pelicula['caracteristicas']):
                eliminada = pelicula['caracteristicas'].pop(idx_car)
                print(f"\nCaracterística '{eliminada}' eliminada.")
            else:
                print("\nÍndice fuera de rango.")
        else:
            print("\nÍndice de película inválido.")
    except ValueError:
        print("\nEntrada inválida. Debe ser un número.")
