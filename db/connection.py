import mysql.connector 
from mysql.connector import Error

class DAO():
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host ='localhost',
                port = 3306,
                user = 'root',
                password ='',
                db = 'calificaciones-dev'        
        )
        except Exception as ex:
            print("Error al intentar conectar la conexion111: {0}".format(ex))
            

    def listUsers(self):
        if self.connection.is_connected():
            try:
               cursor = self.connection.cursor()
               cursor.execute("SELECT * FROM users ORDER BY id ASC")
               result = cursor.fetchall()
               return result
            except Error as ex:
               print("Error al intentar conectar la conexion: {0}".format(ex))
               
    def consultUser(self):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM users WHERE full_name=?", (search_query))
                search_query = cursor.fetchall()
            except Error as ex:
               print("Error al intentar conectar la conexion: {0}".format(ex))

               
