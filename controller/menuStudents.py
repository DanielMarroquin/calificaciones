import os


def menuEstudiantes():
    showMenu = True
    while(showMenu):
        successOption = False
        while(not successOption):
            print("========================= GESTION DE ESTUDIANTES ===================")
            print("1.- Ingresar Estudiante")
            print("2.- Consultar Estudiante")
            print("3.- Editar Estudiante")
            print("4.- Eliminar Estudiante")
            print("5.- Volver al Menu Principal")
            print("====================================================================")
            option = int(input("Seleccione una Opción: "))
            if option < 1 or option > 5:
                print("Opción Incorrecta, ingrese nuevamente...")
            elif option == 5:
                #Se controla la salida del programa
                showMenu = True
                os.system('cls')
                menuPrincipal()
            else:
                successOption = True
                #processOption(option)
                
