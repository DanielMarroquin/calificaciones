from db.connection import DAO
import controller.menuUsers
import controller.menuStudents
import controller.menuScore
import os

def menuPrincipal():
    #Validacion para mostrar el menu
    showMenu = True
    while(showMenu):
        successOption = False
        while(not successOption):
            print("========================= MENÚ PRINCIPAL ===================")
            print("1.- Gestión de Usuarios")
            print("2.- Gestión de Estudiantes")
            print("3.- Gestión de Calificaciones")
            print("4.- Cerrar Sesión")
            print("5.- Salir del Programa")
            print("============================================================")
            option = int(input("Seleccione una Opción: "))
            
            #Validacion para escoger opciones
            if option < 1 or option > 5:
                print("Opción Incorrecta, ingrese nuevamente...")
            elif option == 5:
                #Se controla la salida del programa
                showMenu = False
                print("Gracias por usar el sistema..!!")
                break
            else:
                successOption = True
                processOption(option)
        
def processOption(option):
    dao = DAO()
    
    if option == 1:
        try:
            os.system('cls')
            controller.menuUsers.menuUsuarios().showMenu()
        except:
            os.system('cls')
    elif option == 2:
        try:
            os.system('cls')
            controller.menuStudents.menuEstudiantes().showMenu()
        except:
            os.system('cls')
    elif option == 3:
        try:
            os.system('cls')
            controller.menuScore.menuCalificaciones().showMenu()
        except:
            os.system('cls')
    elif option == 4:
        print("Eliminacion")
    else:
        print("Opcion no valida")
    
    
menuPrincipal()