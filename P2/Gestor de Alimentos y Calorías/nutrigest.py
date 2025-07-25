alimentos = []
frecuentes = {}

perfil_usuario = {
    "nombre": "",
    "edad": 0,
    "peso": 0.0,
    "altura": 0.0,
    "sexo": "",
    "calorias_diarias": 0.0
}

def borrarPantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\nPresiona ENTER para continuar...")

def ingresar_datos_usuario():
    borrarPantalla()
    print("\n\t\t\t .:::DATOS PERSONALES:::.")
    perfil_usuario["nombre"] = input("\n\tNombre: ").strip().title()
    perfil_usuario["edad"] = int(input("\tEdad: "))
    perfil_usuario["peso"] = float(input("\tPeso en kg: "))
    perfil_usuario["altura"] = float(input("\tAltura en cm: "))
    perfil_usuario["sexo"] = input("\tSexo (M/F): ").strip().upper()

    if perfil_usuario["sexo"] == "M":
        tmb = 66 + (13.7 * perfil_usuario["peso"]) + (5 * perfil_usuario["altura"]) - (6.8 * perfil_usuario["edad"])
    else:
        tmb = 655 + (9.6 * perfil_usuario["peso"]) + (1.8 * perfil_usuario["altura"]) - (4.7 * perfil_usuario["edad"])

    perfil_usuario["calorias_diarias"] = round(tmb * 1.5, 2)

    print(f"\n\t✅ Bienvenido/a {perfil_usuario['nombre']}")
    print(f"\t🔥 Calorías recomendadas por día: {perfil_usuario['calorias_diarias']} kcal")

def agregar_alimento():
    borrarPantalla()
    print("\n\t\t\t .:::AGREGAR ALIMENTO:::.")
    print("\n\t📌 Instrucciones:")
    print("\t- Escribe alimentos comunes como 'Arroz cocido', 'Milanesa de pollo', 'Plátano'")
    print("\t- Si no sabes cuántas calorías tiene, pon un estimado (ej. 230 kcal para una milanesa mediana)")
    print("\t- Usa porciones fáciles de entender: 1 pieza, 1 taza, 100g, etc.\n")

    alimento = {}
    alimento['nombre'] = input("\tNombre del alimento: ")
    alimento['tipo'] = input("\tTipo (ej. fruta, verdura, proteína, etc.): ")
    alimento['porcion'] = input("\tTamaño de porción (ej. 1 pieza, 1 taza, 100g): ")
    alimento['cantidad'] = float(input("\t¿Cuántas porciones comiste?: "))
    alimento['calorias_unitarias'] = float(input("\tCalorías por porción (ej. 130): "))
    alimento['calorias_totales'] = alimento['calorias_unitarias'] * alimento['cantidad']

    alimentos.append(alimento)

    nombre_lower = alimento['nombre'].strip().lower()
    if nombre_lower in frecuentes:
        frecuentes[nombre_lower] += 1
    else:
        frecuentes[nombre_lower] = 1

    print(f"\n\t✅ {alimento['nombre']} fue agregado correctamente.")
    print(f"\t   Total de calorías: {alimento['calorias_totales']} kcal")

def mostrar_alimentos():
    borrarPantalla()
    print("\n\t\t\t .:::ALIMENTOS REGISTRADOS:::.")
    if not alimentos:
        print("\n\tNo hay alimentos registrados.")
        return

    for i, alimento in enumerate(alimentos, start=1):
        print(f"\n\t{i}. 🍽️  {alimento['nombre'].upper()}")
        print(f"\t   Tipo: {alimento['tipo']}")
        print(f"\t   Porción: {alimento['porcion']} x {alimento['cantidad']}")
        print(f"\t   Calorías por porción: {alimento['calorias_unitarias']} kcal")
        print(f"\t   🔥 Total calorías: {alimento['calorias_totales']} kcal")
        print("\t" + "-" * 40)

def calcular_calorias():
    borrarPantalla()
    print("\n\t\t\t .:::TOTAL DE CALORÍAS:::.")
    if not alimentos:
        print("\n\tNo hay alimentos para calcular.")
        return

    total = sum(a['calorias_totales'] for a in alimentos)
    promedio = total / len(alimentos)

    print(f"\n\t🔥 TOTAL DE CALORÍAS CONSUMIDAS: {total:.2f} kcal")
    print(f"\t🍽️  Promedio por alimento: {promedio:.2f} kcal")

    if perfil_usuario["calorias_diarias"] > 0:
        diferencia = total - perfil_usuario["calorias_diarias"]
        if diferencia > 0:
            print(f"\t⚠️ Te has pasado por {diferencia:.2f} kcal de tu recomendación diaria.")
        elif diferencia < -300:
            print(f"\tℹ️ Estás por debajo de tu meta calórica por {-diferencia:.2f} kcal.")
        else:
            print(f"\t✅ Vas dentro del rango calórico saludable. ¡Bien!")
    else:
        print("\tℹ️ Ingresa tus datos personales para obtener recomendaciones.")

def mostrar_frecuentes():
    borrarPantalla()
    print("\n\t\t\t .:::ALIMENTOS MÁS FRECUENTES:::.")
    if not frecuentes:
        print("\n\tNo hay datos aún.")
        return

    ordenados = sorted(frecuentes.items(), key=lambda x: x[1], reverse=True)
    for i, (nombre, veces) in enumerate(ordenados[:5], start=1):
        print(f"\n\t{i}. {nombre.title()} - agregado {veces} vez(es)")

def mostrar_menu_principal():
    print("\n" + "=" * 50)
    print("\t\t  🍎 NUTRIGEST - CONTROL NUTRICIONAL")
    print("=" * 50)

    if perfil_usuario["nombre"]:
        print(f"\n\t👤 Usuario: {perfil_usuario['nombre']}")
        print(f"\t🔢 Calorías recomendadas: {perfil_usuario['calorias_diarias']} kcal")

    print("\n\t1. Agregar alimento")
    print("\t2. Mostrar alimentos registrados")
    print("\t3. Calcular calorías totales")
    print("\t4. Ver alimentos más frecuentes")
    print("\t5. Ingresar datos personales")
    print("\t6. Salir del sistema")
    print("\n" + "-" * 50)

def main():
    borrarPantalla()
    print("\n\t\t\t🍎 BIENVENIDO A NUTRIGEST 🍎")
    print("\n\tAntes de comenzar, ingresa tus datos personales.")
    esperarTecla()
    ingresar_datos_usuario()

    while True:
        borrarPantalla()
        mostrar_menu_principal()
        opcion = input("\n\tElige una opción (1-6): ").strip()

        match opcion:
            case "1":
                agregar_alimento()
            case "2":
                mostrar_alimentos()
            case "3":
                calcular_calorias()
            case "4":
                mostrar_frecuentes()
            case "5":
                ingresar_datos_usuario()
            case "6":
                print("\n\t🚪 Saliendo del sistema... ¡Hasta pronto! 🍏")
                break
            case _:
                print("\n\t❌ Opción inválida, vuelve a intentar.")

        esperarTecla()

if __name__ == "__main__":
    main()
    



