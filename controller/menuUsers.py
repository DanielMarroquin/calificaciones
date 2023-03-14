import os
import mysql.connector
from db.connection import DAO
from functions.users import USER

def menuUsuarios():
    showMenu = True
    while(showMenu):
        successOption = False
        while(not successOption):
            print("========================= GESTION DE USUARIOS ===================")
            print("1.- Listar Usuarios")
            print("2.- Crear Usuario")
            print("3.- Editar Usuario")
            print("4.- Eliminar Usuario")
            print("5.- Volver al Menu Principal")
            print("=================================================================")
            option = int(input("Seleccione una Opción: "))
            
            if option < 1 or option > 5:
                print("Opción Incorrecta, ingrese nuevamente...")
            elif option == 5:
                showMenu = True
                os.system('cls')
                #menuPrincipal()
            else:
                successOption = True
                processOption(option)
                
def processOption(option):
    dao = DAO()
    user = USER()
    if option == 1:
        try:
            users = dao.listUsers()
            if len(users) > 0:
                max_lengths = [max(len(str(item[i])) for item in users) for i in range(len(users[0]))]
                headers = "|".join(["{:<{}}".format(header, max_lengths[i]) for i, header in enumerate(["ID", "Nombre", "Usuario", "Clave", "Estado"])])
                table_data = "\n".join([" | ".join(["{:<{}}".format(str(item[i]), max_lengths[i]) for i in range(len(item))]) for item in users])
                print("========= LISTA DE USUARIOS ========")
                print(headers)
                print("-" * len(headers))
                print(table_data)
            else:
                print("No se encontraron usuarios...")
        except:
            print("Error opcion 1...")
    elif option == 2:
        user = user.createUserGetData()
        try:
            dao.createUser(user)
        except:
            print("Error opcion 2...")

            
        


            
            
                
    
    
    
    
    