



class Calification(Estudiante):
    def __init__(self, cedula, nombre, apellido, correo, celular, nota1, nota2, nota3, nota4):
        super().__init__(cedula, nombre, apellido, correo, celular)
        self.notas = []
        self.agregar_nota(nota1, "1")
        self.agregar_nota(nota2, "2")
        self.agregar_nota(nota3, "3")
        self.agregar_nota(nota4, "4")

    def agregar_nota(self, nota, num_nota):
        nota_regex = r'^\d+(\.\d+)?$'
        while True:
            if re.match(nota_regex, nota):
                nota = float(nota)
                if nota < 0 or nota > 100:
                    print(f"La nota {num_nota} debe estar entre 0 y 100.")
                    nota = input(f"Ingrese la nota {num_nota} correctamente: ")
                else:
                    self.notas.append(nota)
                    break
            else:
                print(f"La nota {num_nota} debe ser un número válido.")
                nota = input(f"Ingrese la nota {num_nota} correctamente: ")

    def calification_notas(self):
        if len(self.notas) == 0:
            return 0
        else:
            return sum(self.notas) / len(self.notas)

username = input("Ingrese el nombre de usuario: ")
password = input("Ingrese la contraseña: ")
cedula = input("Ingrese la cédula del estudiante: ")
nombre = input("Ingrese el nombre del estudiante: ")
apellido = input("Ingrese el apellido del estudiante: ")
correo = input("Ingrese el correo del estudiante: ")
celular = input("Ingrese el celular del estudiante: ")
nota1 = input("Ingrese la nota 1: ")
nota2 = input("Ingrese la nota 2: ")
nota3 = input("Ingrese la nota 3: ")
nota4 = input("Ingrese la nota 4: ")
estudiante = Calification(cedula, nombre, apellido, correo, celular, nota1, nota2, nota3, nota4)

promedio = estudiante.calification_notas()
if promedio is None:
    print("No existen notas para este estudiante.")
else:
    print("El promedio de las notas es:", promedio)