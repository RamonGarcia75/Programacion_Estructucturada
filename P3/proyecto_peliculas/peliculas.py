import mysql.connector
from mysql.connector import Error

#Dict u objeto que permita almacenar los siguientes atributos: (nombre,categoria,clasificacion,genero,idioma) de peliculas

# pelicula={
#             "nombre":"",
#             "categoria":"",
#             "clasificacion":"",
#             "genero":"",
#             "idioma":""
#          }

pelicula={}

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
   input("\n\t ... Oprima cualquier tecla para continuar ...")

def conectar():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_peliculas"
        )
        return conexion
    except Error as e:
        print(f"El error que se presenta es: {e}")
        return None

def crearPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
        print("\n\t .:: Agregar Películas ::.\n")
        pelicula.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
        #pelicula["nombre"]=input("Ingresa el nombre: ").upper().strip()
        pelicula.update({"categoria":input("Ingresa la categoría: ").upper().strip()})
        pelicula.update({"clasificacion":input("Ingresa la clasificación: ").upper().strip()})
        pelicula.update({"genero":input("Ingresa el genero: ").upper().strip()})
        pelicula.update({"idioma":input("Ingresa el idioma: ").upper().strip()})
        ######## SQL a BD
        cursor=conexionBD.cursor()
        sql="insert into peliculas ( nombre, categoria, clasificacion, genero, idioma) values ( %s, %s, %s, %s, %s)"
        val=(pelicula["nombre"],pelicula["categoria"],pelicula["clasificacion"],pelicula["genero"],pelicula["idioma"])
        cursor.execute(sql,val)
        conexionBD.commit()
        print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON EXÍTO! :::")
    
def mostrarPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
      cursor=conexionBD.cursor()
      sql="select * from peliculas"
      cursor.execute(sql,)
      registros=cursor.fetchall()
      print("\n\t .:: Mostrar Películas ::.\n")
      if registros:
        print(f"\n\tMostrar las Peliculas")
        print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
        print(f"-"*80)
        for fila in registros:
          print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
        print(f"-"*80)  
      else:
        print("\n\t .:: No hay peliculas en el Sistema ::. ")      

def buscarPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
      nombre=input("Dame el nombre de la pelicula a buscar: ").upper().strip()
      cursor=conexionBD.cursor()
      sql="select * from peliculas where nombre=%s"
      val=(nombre,)
      cursor.execute(sql,val)
      registros=cursor.fetchall()
      if registros:
        print(f"\n\tMostrar las Peliculas")
        print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
        print(f"-"*80)
        for fila in registros:
          print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
        print(f"-"*80)  
      else:
        print("\n\t .:: No hay peliculas en el Sistema con ese nombre::. ")    

def borrarPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
      nombre=input("Dame el nombre de la pelicula a borrar: ").upper().strip()
      cursor=conexionBD.cursor()
      sql="select * from peliculas where nombre=%s"
      val=(nombre,)
      cursor.execute(sql,val)
      registros=cursor.fetchall()
      if registros:
        print(f"\n\tMostrar las Peliculas")
        print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
        print(f"-"*80)
        for fila in registros:
          print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
        print(f"-"*80) 
        resp=input(f"¿Deseas borrar la pelicula {nombre}? (Si/No): " ).lower().strip()
        if resp=="si":
           sql="delete from peliculas where nombre=%s"
           val=(nombre,)
           cursor.execute(sql,val)
           conexionBD.commit()
           print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON EXÍTO! :::")
      else:
        print("\n\t .:: No hay peliculas en el Sistema con ese nombre::. ")   

def modificarPeliculas():
    borrarPantalla()
    conexionBD=conectar()
    if conexionBD!=None:
      nombre=input("Dame el nombre de la pelicula a modificar: ").upper().strip()
      cursor=conexionBD.cursor()
      sql="select * from peliculas where nombre=%s"
      val=(nombre,)
      cursor.execute(sql,val)
      registros=cursor.fetchall()
      if registros:
        print(f"\n\tMostrar las Peliculas")
        print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
        print(f"-"*80)
        for fila in registros:
          print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
        print(f"-"*80) 
        resp=input(f"¿Deseas modificar la pelicula {nombre}? (Si/No): " ).lower().strip()
        if resp=="si":
           nuevo_nombre=input("Ingresa el nuevo nombre: ").upper().strip()
           nueva_categoria=input("Ingresa la nueva categoria: ").upper().strip()
           nueva_clasificacion=input("Ingresa la nueva clasificacion: ").upper().strip()
           nuevo_genero=input("Ingresa el nuevo genero: ").upper().strip()
           nuevo_idioma=input("Ingresa el nuevo idioma: ").upper().strip()
           sql="update peliculas set nombre= %s categoria=%s, clasificacion=%s, genero=%s, idioma=%s where nombre=%s"
           val=(nuevo_nombre, nueva_categoria,nueva_clasificacion,nuevo_genero,nuevo_idioma,nombre)
           cursor.execute(sql,val)
           conexionBD.commit()
           print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON EXÍTO! :::")
      else:
        print("\n\t .:: No hay peliculas en el Sistema con ese nombre::. ")