import mysql.connector
from mysql.connector import Error

def borrarPantalla():
    import os
    os.system('cls')

def esperar_Tecla():
    input("\n\t\t\t\t\t👉 Oprima cualquier tecla para continuar...")

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_agenda"
        )
        return conexion
    except Error as e:
        print(f"El error que se presenta es: {e}")
        return None
    
def menu_principal():
    borrarPantalla()
    print("\t\t\t\t 📝.::: Sistema de Gestión de Agenda de Contactos :::. 📝\n")
    print("\t\t\t\t\t 1️⃣  Agregar contacto")
    print("\t\t\t\t\t 2️⃣  Mostrar todos los contactos")
    print("\t\t\t\t\t 3️⃣  Buscar contacto por nombre")
    print("\t\t\t\t\t 4️⃣  Modificar contacto")
    print("\t\t\t\t\t 5️⃣  Eliminar contacto")
    print("\t\t\t\t\t 6️⃣  Salir del programa")
    opcion = input("\n\t\t\t\t\t👉 Elige una opción de (1-4): ")
    return opcion

def agregar_contacto():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
            print("\n\t\t\t\t\t📝 Agregar Contacto")
            nombre = input("\t\t\t\t\t👉 Nombre del contacto: ").upper().strip()
            telefono = input("\t\t\t\t\t👉 Teléfono del contacto: ").upper().strip()
            email = input("\t\t\t\t\t👉 Correo electrónico del contacto: ").lower().strip()
            cursor = conexionBD.cursor()
            sql = "INSERT INTO contactos (nombre, telefono, email) VALUES (%s, %s, %s)"
            val = (nombre, telefono, email)
            cursor.execute(sql, val)
            conexionBD.commit()
            print("\n\t\t\t\t\t✅ Contacto agregado con éxito.")
    else:
        print("\n\t\t\t\t\t❌ No se pudo conectar a la base de datos.")

def mostrar_contactos():
    borrarPantalla()
    print("\n\t\t\t\t\t📂 Mostrar Contactos")
    conexionBD = conectar()
    if conexionBD is not None:
        cursor = conexionBD.cursor()
        sql = "SELECT * FROM contactos"
        cursor.execute(sql)
        registros = cursor.fetchall()
        if registros:
            print(f"\n\t\t\t\t\t{'ID':<5}{'Nombre':<20}{'Teléfono':<20}{'Correo':<30}")
            print("-"*60)
            for fila in registros:
                print(f"\t\t\t\t\t{fila[0]:<5}{fila[1]:<20}{fila[2]:<20}{fila[3]:<30}")
            print("-"*60)
        else:
            print("\n\t\t\t\t\t❌ No hay contactos en la agenda.")
    else:
        print("\n\t\t\t\t\t❌ No se pudo conectar a la base de datos.")

def buscar_contacto():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        print("\n\t\t\t\t\t🔍 Buscar Contacto")
        nombre = input("\t\t\t\t\t👉 Nombre del contacto a buscar: ").upper().strip()
        cursor = conexionBD.cursor()
        sql = "SELECT * FROM contactos WHERE nombre = %s"
        val = (nombre,)
        cursor.execute(sql, val)
        registros = cursor.fetchall()
        if registros:
            print(f"\n\t\t\t\t\t{'ID':<5}{'Nombre':<20}{'Teléfono':<20}{'Correo':<30}")
            print("-"*60)
            for fila in registros:
                print(f"\t\t\t\t\t{fila[0]:<5}{fila[1]:<20}{fila[2]:<20}{fila[3]:<30}")
            print("-"*60)
            print("\n\t\t\t\t\t✅ Contacto encontrado.")
        else:
            print("\n\t\t\t\t\t❌ El contacto no existe.")
    else:
        print("\n\t\t\t\t\t❌ No se pudo conectar a la base de datos.")

def modificar_contacto():
    borrarPantalla()
    print("\n\t\t\t\t\t✏️ Modificar Contacto")
    conexionBD = conectar()
    if conexionBD is not None:
        nombre = input("\t\t\t\t\t👉 Nombre del contacto a buscar: ").upper().strip()
        cursor = conexionBD.cursor()
        sql = "SELECT * FROM contactos WHERE nombre = %s"
        val = (nombre,)
        cursor.execute(sql, val)
        registro = cursor.fetchone()
        if registro:
            print("Valores actuales:")
            print(f"Nombre: {registro[1]}\n Teléfono: {registro[2]}\n E-mail: {registro[3]}")
            respuesta = input("\t\t\t\t\t👉 ¿Desea modificar el contacto? (Si/No): ").lower().strip()
            if respuesta == "si":
                telefono = input("\t\t\t\t\t👉 Nuevo teléfono del contacto: ").upper().strip()
                email = input("\t\t\t\t\t👉 Nuevo correo electrónico del contacto: ").lower().strip()
                sql_update = "UPDATE contactos SET telefono = %s, email = %s WHERE nombre = %s"
                val_update = (telefono, email, nombre)
                cursor.execute(sql_update, val_update)
                conexionBD.commit()
                print("\n\t\t\t\t\t✅ Contacto modificado con éxito.")
            else:
                print("\n\t\t\t\t\t❌ Modificación cancelada.")
        else:
            print("\n\t\t\t\t\t❌ El contacto no existe.")
        conexionBD.close()
    else:
        print("\n\t\t\t\t\t❌ No se pudo conectar a la base de datos.")

def eliminar_contacto():
    borrarPantalla()
    print("\n\t\t\t\t\t🗑️ Eliminar Contacto")
    conexionBD = conectar()
    if conexionBD is not None:
        nombre = input("\t\t\t\t\t👉 Nombre del contacto a eliminar: ").upper().strip()
        cursor = conexionBD.cursor()
        sql = "SELECT * FROM contactos WHERE nombre = %s"
        val = (nombre,)
        cursor.execute(sql, val)
        registro = cursor.fetchone()
        if registro:
            respuesta = input(f"\t\t\t\t\t👉 ¿Está seguro de eliminar el contacto {nombre}? (Si/No): ").lower().strip()
            if respuesta == "si":
                sql_delete = "DELETE FROM contactos WHERE nombre = %s"
                cursor.execute(sql_delete, val)
                conexionBD.commit()
                print("\n\t\t\t\t\t✅ Contacto eliminado con éxito.")
            else:
                print("\n\t\t\t\t\t❌ Eliminación cancelada.")
        else:
            print("\n\t\t\t\t\t❌ El contacto no existe.")
        conexionBD.close()
    else:
        print("\n\t\t\t\t\t❌ No se pudo conectar a la base de datos.")