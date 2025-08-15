from database import conectar_db, cerrar_db
import os
from datetime import datetime

def borrar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperar_tecla():
    input("\nPresiona ENTER para continuar...")
    borrar_pantalla()

def registrar_usuario():
    conexion = conectar_db()
    if not conexion:
        return
    try:
        borrar_pantalla()
        print("\n" + "="*50)
        print(" REGISTRO DE NUEVO USUARIO ".center(50))
        print("="*50)
        
        datos = {
            'nombre': input("Nombre completo: ").strip().title(),
            'edad': int(input("Edad: ")),
            'peso': float(input("Peso (kg): ")),
            'altura': float(input("Altura (cm): ")),
            'sexo': input("Sexo (M/F): ").strip().upper()
        }

        if datos['sexo'] == "M":
            tmb = 88.362 + (13.397 * datos['peso']) + (4.799 * datos['altura']) - (5.677 * datos['edad'])
        else:
            tmb = 447.593 + (9.247 * datos['peso']) + (3.098 * datos['altura']) - (4.330 * datos['edad'])
        
        datos['calorias_diarias'] = round(tmb * 1.55)  # Actividad moderada

        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO usuarios (nombre, edad, peso, altura, sexo, calorias_diarias)
            VALUES (%(nombre)s, %(edad)s, %(peso)s, %(altura)s, %(sexo)s, %(calorias_diarias)s)
        """, datos)
        conexion.commit()
        
        print(f"\n✅ Usuario registrado correctamente (ID: {cursor.lastrowid})")
        print(f"🔥 Calorías diarias recomendadas: {datos['calorias_diarias']} kcal")
        print("\n⚠️ ¡Anota tu ID de usuario para futuras operaciones!")

    except ValueError:
        print("\n❌ Error: Ingresa datos numéricos válidos")
    except Exception as e:
        print(f"\n❌ Error inesperado: {str(e)}")
    finally:
        cerrar_db(conexion)
        esperar_tecla()

def agregar_alimento():
    conexion = conectar_db()
    if not conexion: 
        return

    try:
        borrar_pantalla()
        print("\n" + "="*50)
        print(" REGISTRO DE ALIMENTO ".center(50))
        print("="*50)
        
        # Mostrar usuarios
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT id, nombre FROM usuarios")
        usuarios = cursor.fetchall()
        
        if not usuarios:
            print("\n❌ No hay usuarios registrados")
            esperar_tecla()
            return
            
        print("\nUsuarios disponibles:")
        for usuario in usuarios:
            print(f"ID: {usuario['id']} - Nombre: {usuario['nombre']}")
        
        usuario_id = input("\nIngrese ID del usuario: ").strip()
        
        # Verificar usuario
        cursor.execute("SELECT id FROM usuarios WHERE id = %s", (usuario_id,))
        if not cursor.fetchone():
            print("\n❌ ID de usuario no válido")
            esperar_tecla()
            return

        # Datos del alimento
        alimento = {
            'nombre': input("\nNombre del alimento: ").strip().title(),
            'tipo': input("Tipo (fruta/verdura/proteína...): ").strip().lower(),
            'es_por_peso': input("¿Es por peso? (s/n): ").strip().lower() == 's'
        }

        if alimento['es_por_peso']:
            alimento['cantidad'] = float(input("Gramos consumidos: "))
            calorias = float(input("Calorías por 100g: "))
            alimento['calorias_totales'] = (alimento['cantidad'] / 100) * calorias
            alimento['calorias_por_100g'] = calorias
            alimento['calorias_por_unidad'] = None
        else:
            alimento['cantidad'] = int(input("Unidades consumidas: "))
            calorias = float(input("Calorías por unidad: "))
            alimento['calorias_totales'] = alimento['cantidad'] * calorias
            alimento['calorias_por_unidad'] = calorias
            alimento['calorias_por_100g'] = None

        # Insertar alimento en la tabla con usuario_id
        cursor.execute("""
            INSERT INTO alimentos (nombre, tipo, calorias_por_100g, calorias_por_unidad, es_por_peso, usuario_id)
            VALUES (%(nombre)s, %(tipo)s, %(calorias_por_100g)s, %(calorias_por_unidad)s, %(es_por_peso)s, %(usuario_id)s)
        """, {
            'nombre': alimento['nombre'],
            'tipo': alimento['tipo'],
            'calorias_por_100g': alimento['calorias_por_100g'],
            'calorias_por_unidad': alimento['calorias_por_unidad'],
            'es_por_peso': alimento['es_por_peso'],
            'usuario_id': usuario_id
        })

        alimento_id = cursor.lastrowid

        # Registrar consumo en registros_diarios
        cursor.execute("""
            INSERT INTO registros_diarios (usuario_id, alimento_id, cantidad, calorias_totales, fecha)
            VALUES (%s, %s, %s, %s, CURDATE())
        """, (usuario_id, alimento_id, alimento['cantidad'], alimento['calorias_totales']))
        
        conexion.commit()
        
        print(f"\n✅ {alimento['nombre']} registrado: {alimento['calorias_totales']:.2f} kcal")
        esperar_tecla()

    except ValueError:
        print("\n❌ Error: Ingresa valores numéricos válidos")
        esperar_tecla()
    except Exception as e:
        print(f"\n❌ Error inesperado: {str(e)}")
        esperar_tecla()
    finally:
        cerrar_db(conexion)

def generar_reporte():
    conexion = conectar_db()
    if not conexion:
        return
    try:
        borrar_pantalla()
        print("\n" + "="*50)
        print(" REPORTE DIARIO ".center(50))
        print("="*50)

        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT id, nombre FROM usuarios")
        usuarios = cursor.fetchall()
        
        if not usuarios:
            print("\n❌ No hay usuarios registrados")
            return
        
        print("\nUsuarios disponibles:")
        for usuario in usuarios:
            print(f"ID: {usuario['id']} - Nombre: {usuario['nombre']}")
        
        usuario_id = input("\nIngrese ID del usuario: ")
        cursor.execute("SELECT * FROM usuarios WHERE id = %s", (usuario_id,))
        usuario = cursor.fetchone()
        
        if not usuario:
            print("\n❌ Usuario no encontrado")
            return

        cursor.execute("""
            SELECT a.nombre, r.cantidad, r.calorias_totales, r.fecha, a.es_por_peso
            FROM registros_diarios r
            JOIN alimentos a ON r.alimento_id = a.id
            WHERE r.usuario_id = %s AND r.fecha = CURDATE()
        """, (usuario_id,))
        alimentos = cursor.fetchall()

        total_calorias = sum(a['calorias_totales'] for a in alimentos) if alimentos else 0
        
        print(f"\n👤 Usuario: {usuario['nombre']}")
        print(f"📅 Fecha: {datetime.now().strftime('%d/%m/%Y')}")
        print(f"🔥 Calorías recomendadas: {usuario['calorias_diarias']} kcal")
        
        print("\n🍽️ Alimentos consumidos hoy:")
        for alimento in alimentos:
            unidad = "g" if alimento['es_por_peso'] else "unid."
            print(f"- {alimento['nombre']}: {alimento['cantidad']}{unidad} ({alimento['calorias_totales']:.2f} kcal)")
        
        print(f"\n📊 TOTAL HOY: {total_calorias:.2f} kcal")
        diferencia = total_calorias - usuario['calorias_diarias']
        print(f"{'⚠️ Exceso' if diferencia>0 else '✅ Balance'}: {abs(diferencia):.2f} kcal")

    except Exception as e:
        print(f"\n❌ Error generando reporte: {str(e)}")
    finally:
        cerrar_db(conexion)
        esperar_tecla()
