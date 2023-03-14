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
            
            
    #Seccion para modulo de usuarios
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
               
               
    def createUser(self, user):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "INSERT INTO users (id, full_name, username, password, status) VALUES ('{0}, '{1}', {2})"
                cursor.execute(sql.format(user[0], user[1], user[2], user[3], user[4]))
                self.connection.commit()
                print("Usuario registrado correctamente..!!\n")
            except Error as ex:
                print("Error al intentar conectar la conexion: {0}".format(ex))
               
    def deleteUser(self):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("DELETE FROM users WHERE id = '{0}'")
                self.connection.commit()
                print("Usuario Eliminado..!!\n")
            except Error as ex:
                print("Error al intentar conectar la conexion: {0}".format(ex))
                
    def updateUser(self):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "UPDATE users SET full_name = '{0}', username = '{1}' where id = '{2}'"
                cursor.execute(sql.format(user[1], user[2], user[0]))
                self.connection.commit()
                print("Usuario Actualizado..!!\n")
            except Error as ex:
                print("Error al intentar conectar la conexion: {0}".format(ex))
                

               
