class Estudiante:

    def __init__(self, cedula, nombre, apellido, correo, celular):
        self.cedula = self.validar_cedula(cedula)
        self.nombre = self.validar_nombre(nombre)
        self.apellido = self.validar_apellido(apellido)
        self.correo = correo
        self.celular = self.validar_celular(celular)

    def validar_cedula(self, cedula):
        while True:
            if re.match(r'^\d{10}$', cedula):
                return cedula
            else:
                cedula = input("La cédula debe tener 10 dígitos. Ingrese la cédula nuevamente: ")

    def validar_nombre(self, nombre):
        while True:
            if re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
                return nombre
            else:
                nombre = input("El nombre  no puede contener números ni caracteres especiales. Ingrese el nombre nuevamente: ")

    def validar_apellido(self, apellido):
        while True:
            if re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', apellido):
                return apellido
            else:
                apellido = input("El apellido no puede contener números ni caracteres especiales: ")
    def validar_celular(self, celular):
        while True:
            if re.match(r'^\d{10}$', celular):
                return celular
            else:
                celular = input("El número de celular debe tener 10 dígitos. Ingrese el número de celular nuevamente: ")