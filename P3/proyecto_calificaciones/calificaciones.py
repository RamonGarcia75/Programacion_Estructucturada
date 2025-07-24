import mysql.connector
from mysql.connector import Error

def borrarPantalla():
    import os
    os.system('cls')

def esperarTecla():
    input("\t\t\t\t⌛ ...Oprima cualquier tecla para continuar... ⏳")

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_calificaciones"
        )
        return conexion
    except Error as e:
        print(f"El error que se presenta es: {e}")
        return None

def menu_principal():
    print("\t\t\t\t 📝 .::: SISTEMA DE CALIFICACIONES :::. 📝\n")
    print("\t\t\t\t\t 1️⃣  ➤  Agregar")
    print("\t\t\t\t\t 2️⃣  ➤  Mostrar")
    print("\t\t\t\t\t 3️⃣  ➤  Calcular Promedio")
    print("\t\t\t\t\t 4️⃣  ➤  Buscar")
    print("\t\t\t\t\t 5️⃣  ➤  Salir\n")
    opcion = input("\t\t\t\t\t🔍 Selecciona una opción de 1-4: ")
    return opcion

def agregarAlumno():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD:
        print("\n\t .:: Agregar Alumno ::.\n")
        nombre = input("Ingresa el nombre del alumno: ").upper().strip()
        
        calificaciones = []
        for i in range(1, 4):
            while True:
                try:
                    cal = float(input(f"Ingrese la calificación {i}: "))
                    if 0 <= cal <= 10:
                        calificaciones.append(cal)
                        break
                    else:
                        print("❌ Calificación fuera de rango (0-10).")
                except ValueError:
                    print("❌ Ingresa un número válido.")

        cursor = conexionBD.cursor()
        sql = "INSERT INTO alumnos (nombre, calif1, calif2, calif3) VALUES (%s, %s, %s, %s)"
        val = (nombre, calificaciones[0], calificaciones[1], calificaciones[2])
        cursor.execute(sql, val)
        conexionBD.commit()
        print("\n\t✅ ¡Alumno registrado con éxito!")
        esperarTecla()

def mostrarAlumnos():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD:
        cursor = conexionBD.cursor()
        cursor.execute("SELECT * FROM alumnos")
        registros = cursor.fetchall()
        print("\n\t .:: Lista de Alumnos ::.\n")
        if registros:
            print(f"{'ID':<5}{'Nombre':<20}{'Calif1':<10}{'Calif2':<10}{'Calif3':<10}")
            print("-"*60)
            for fila in registros:
                print(f"{fila[0]:<5}{fila[1]:<20}{fila[2]:<10}{fila[3]:<10}{fila[4]:<10}")
            print("-"*60)
        else:
            print("⚠️  No hay alumnos registrados.")

def calcularPromedios():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD:
        cursor = conexionBD.cursor()
        cursor.execute("SELECT nombre, calif1, calif2, calif3 FROM alumnos")
        registros = cursor.fetchall()
        print("\n\t .:: Promedios por Alumno ::.\n")
        if registros:
            total = 0
            print(f"{'Nombre':<20}{'Promedio':<10}")
            print("-"*30)
            for fila in registros:
                promedio = (fila[1] + fila[2] + fila[3]) / 3
                total += promedio
                print(f"{fila[0]:<20}{promedio:<10.2f}")
            promedio_grupal = total / len(registros)
            print("-"*30)
            print(f"\nPromedio grupal: {promedio_grupal:.2f}")
        else:
            print("⚠️  No hay alumnos para calcular promedios.")
        conexionBD.close()
        esperarTecla()

def buscarAlumno():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD:
        nombre = input("Ingresa el nombre del alumno a buscar: ").upper().strip()
        cursor = conexionBD.cursor()
        sql = "SELECT * FROM alumnos WHERE nombre = %s"
        cursor.execute(sql, (nombre,))
        registro = cursor.fetchone()
        if registro:
            print(f"\nID: {registro[0]}")
            print(f"Nombre: {registro[1]}")
            print(f"Calif1: {registro[2]}, Calif2: {registro[3]}, Calif3: {registro[4]}")
        else:
            print("⚠️  Alumno no encontrado.")
        conexionBD.close()
        esperarTecla()