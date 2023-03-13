from mysql.connector import Error

class USER():
    
    # def listUsers(self):
    #     if self.connection.is_connected():
    #         if connection.is_connected():
    #             print("Conexion Exitosa")
    #         try:
    #             cursor = self.connection.cursor()
    #             cursor.execute("SELECT * FROM users ORDER BY id DESC")
    #             result = cursor.fetchall()
    #             return result
    #             print("resewdew", result)
    #         except Error as ex:
    #             print("Error al intentar la conexión: {0}".format(ex))


    def findAllUsers(users):
        print("\nUsuarios: \n")
        counts = 1
        for user in users:
            print(tabulate([ ['id', users[0]], ['full_name', users[1] ]]))
            # data = "{0}. id: {1} | full_name: {2} | {3} username"
            # print(data)
            # print(data.format(counts, use[0], use[1], use[2], use[3]))
            # counts = counts + 1
        print(" ")
        
        
#User()
#listUsers()