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
                db = 'calificaciones'        
        )
            if self.connection.is_connected():
                print("Exitosa")
            
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
                
    #Seccion para manejo de estudiantes
    def listStudents(self):
        if self.connection.is_connected():
            try:
               cursor = self.connection.cursor()
               cursor.execute("SELECT * FROM estudiantes ORDER BY id ASC")
               result = cursor.fetchall()
               return result
            except Error as ex:
               print("Error al intentar conectar la conexion: {0}".format(ex))
                
    def createStudent(self, student):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "INSERT INTO estudiantes (id, cedula, nombre, apellido, correo, celular, estado) VALUES ('{0}, '{1}', {2}, {3}, {4}, {5}, {6})"
                cursor.execute(sql.format(user[0], user[1], user[2], user[3], user[4], user[5], user[6]))
                self.connection.commit()
                print("Estudiante registrado correctamente..!!\n")
            except Error as ex:
                print("Error al intentar conectar la conexion: {0}".format(ex))
                
    def deleteStudent(self):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("DELETE FROM estudiantes WHERE id = '{0}'")
                self.connection.commit()
                print("Estudiante Eliminado..!!\n")
            except Error as ex:
                print("Error al intentar conectar la conexion: {0}".format(ex))
                
    def updateStudent(self):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "UPDATE estudiante SET cedula = '{0}', nombre = '{1}' where id = '{2}'"
                cursor.execute(sql.format(student[1], student[2], student[0]))
                self.connection.commit()
                print("Estudiante Actualizado..!!\n")
            except Error as ex:
                print("Error al intentar conectar la conexion: {0}".format(ex))
                
    
    #Seccion para manejo de calificaciones
    def listCalificaciones(self):
        if self.connection.is_connected():
            try:
               cursor = self.connection.cursor()
               cursor.execute("SELECT * FROM calificaciones ORDER BY id ASC")
               result = cursor.fetchall()
               return result
            except Error as ex:
               print("Error al intentar conectar la conexion: {0}".format(ex))
               
    
    def createCalificaciones(self):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "INSERT INTO calificaciones (id, nota_1, nota_2, nota_3, nota_4 ) VALUES ('{0}, '{1}', {2}, {3}, {4})"
                cursor.execute(sql.format(user[0], user[1], user[2], user[3], user[4]))
                self.connection.commit()
                print("Calificaciones registradas correctamente..!!\n")
            except Error as ex:
                print("Error al intentar conectar la conexion: {0}".format(ex))
                
    def deleteCalificacion(self):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute("DELETE FROM calificaciones WHERE id = '{0}'")
                self.connection.commit()
                print("Calificacion eliminada..!!\n")
            except Error as ex:
                print("Error al intentar conectar la conexion: {0}".format(ex))
                
                
    def updateCalificacion(self):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "UPDATE calificaciones SET nota_1 = '{0}', nota_2 = '{1}', nota_3 = '{2}', nota_4 = '{3}', where id_estudiante = '{4}'"
                cursor.execute(sql.format(score[0], score[1], score[2], score[3], score[4]))
                self.connection.commit()
                print("Calificaciones Actualizadas..!!\n")
            except Error as ex:
                print("Error al intentar conectar la conexion: {0}".format(ex))