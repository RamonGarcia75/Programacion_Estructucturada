import mysql.connector
from mysql.connector import Error

def conectar_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",   # Pon tu contraseña si tienes
            database="nutrigest_db"
        )
    except Error as e:
        print(f"❌ Error de conexión: {e}")
        return None

def cerrar_db(conexion):
    if conexion and conexion.is_connected():
        conexion.close()
