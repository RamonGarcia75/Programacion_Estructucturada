agenda_contactos = {}

def borrarPantalla():
    import os
    os.system('cls')

def esperar_Tecla():
    input("\n\t\t\t\t\t👉 Oprima cualquier tecla para continuar...")

def menu_principal():
    borrarPantalla()
    print("\t\t\t\t 📝.::: Sistema de Gestión de Agenda de Contactos :::. 📝\n")
    print("\t\t\t\t\t 1️⃣  Agregar contacto")
    print("\t\t\t\t\t 2️⃣  Mostrar todos los contactos")
    print("\t\t\t\t\t 3️⃣  Buscar contacto")
    print("\t\t\t\t\t 4️⃣  Salir")
    opcion = input("\n\t\t\t\t\t👉 Elige una opción de (1-4): ")
    return opcion

def agregar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t\t\t\t📝 Agregar Contacto")
    nombre = input("\t\t\t\t\t👉 Nombre del contacto: ").upper().strip()
    if nombre in agenda:
        print("\n\t\t\t\t\t❌ El contacto ya existe.")
    else:
        telefono = input("\t\t\t\t\t👉 Teléfono del contacto: ").upper().strip()
        email = input("\t\t\t\t\t👉 Correo electrónico del contacto: ").lower().strip()
        agenda[nombre] =[telefono, email]
        print("\n\t\t\t\t\t✅ Accion realizada con éxito.")

def mostrar_contactos(agenda):
    borrarPantalla()
    print("\n\t\t\t\t\t📂 Mostrar Contactos")
    if not agenda:
        print("\n\t\t\t\t\t❌ No hay contactos en la agenda.")
    else:
        print(f"\n\t\t\t\t\t{'Nombre':<15} {'Teléfono':<15} {'Correo':<10}")
        print(f"-"*60)
        for nombre,datos in agenda.items():
            print(f"{nombre:<15} {datos[0]:<15} {datos[1]:<10}")
        print(f"-"*60)

def buscar_contacto(agenda):
    borrarPantalla()
    print("\n\t\t\t\t\t🔍 Buscar Contacto")
    nombre = input("\t\t\t\t\t👉 Nombre del contacto a buscar: ").upper().strip()
    if nombre in agenda.items():
        print(f"\n\t\t\t\t\t{'Nombre':<15} {'Teléfono':<15} {'Correo':<10}")
        print(f"-"*60)
        for nombre,datos in agenda.items():
            print(f"{nombre:<15} {datos[0]:<15} {datos[1]:<10}")
        print(f"-"*60)
    else:
        print("El nombre no existe")
        