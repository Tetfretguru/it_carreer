import sys
sys.path.append ('/Users/Martin/Library/Caches/pip/wheels/7e/5b/53/30085c62689dcfce50c8f40759945a49eb856af082e9ebf751/psycopg2')
import psycopg2
'''from 30085c62689dcfce50c8f40759945a49eb856af082e9ebf751.psycopg2-2.8.4-cp37-cp37m-macosx_10_14_x86_64.whl import psycopg2'''
conexion1 = psycopg2.connect(database="enfermeros", user="postgres", password="carito") #carga los datos preferentes de la misma DB en un string, similar a cualquier otro lenguaje
cursor = conexion1.cursor()   #se crea una funcion para trabajar con la conexion previamente hecha
sql = "insert into personal(nombre, cedula) values (%s,%s)"    #la consulta se asigna a una variable str... pero sin los valores )es uno de los metodos)
datos = ("Ghiena" , 46016102)    #los datos o valores se cargan en una variable publica 
cursor.execute(sql , datos)   #los parametros de la funcion execute() son las variables que cargamos en los pasos anteriores
datos = ("Morales" , 41168332)
cursor.execute(sql , datos)
conexion1.commit()
conexion1.close()
#si queremos que todo este procedimiento se repita, solo debemos estructurar una secuencia de iteracion