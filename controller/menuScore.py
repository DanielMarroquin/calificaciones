


def menuCalificaciones():
    showMenu = True
    while(showMenu):
        successOption = False
        while(not successOption):
            print("========================= GESTION DE CALIFICACIONES =================")
            print("1.- Ingresar Calificaciones por Estudiante")
            print("2.- Listar Notas de Estudiantes")
            print("3.- Consulta Notas por Estudiante")
            print("4.- Editar Notas por Estudiante")
            print("5.- Eliminar Notas por Estudiante")
            print("6.- Volver al Menu Principal")
            print("=====================================================================")
            option = int(input("Seleccione una Opción: "))
            if option < 1 or option > 6:
                print("Opción Incorrecta, ingrese nuevamente...")
            elif option == 6:
                #Se controla la salida del programa
                showMenu = True
                os.system('cls')
                menuPrincipal()
            else:
                successOption = True
                #processOption(option)