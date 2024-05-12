#retomar la clase padre y sus ramificaciones del programa anterior y agregar condicionales a modo que solo admita respuestas logicas como entradas
operadores = ['+', '-', '*', '/', '%', '**', '//', '<', '>', '=', "#"] 

class estudiante():
    def __init__(self, nombre, num_cuenta, aula, num_materias):
        if nombre not in operadores and all(caracter.isalpha() or caracter.isspace() for caracter in nombre):
            self.nombre = nombre
        else:
            print("El nombre del alumno no es válido")
            self.nombre = None
            
        if len(str(num_cuenta)) == 8 or str(num_cuenta).isdigit():
            self.num_cuenta = num_cuenta
        else:
            print("El número de cuenta no es válido")
            self.num_cuenta = None
            
        if aula in operadores:
            print("El aula no es válida")
            self.aula = None
        else:
            self.aula = aula
     
        if num_materias in operadores or str(num_materias).isalpha():
            print("El número de materias no es válido")
            self.num_materias = None
        else:
            self.num_materias = num_materias

    def mostrar_informacion(self):
        return f"Nombre del alumno: {self.nombre}, Número de cuenta: {self.num_cuenta}, aula: {self.aula}, numero de materias: {self.num_materias}"

class fisico(estudiante):
    def __init__(self, nombre, num_cuenta, aula, num_materias, nombre_libro_especifico):
        super().__init__(nombre, num_cuenta, aula, num_materias)
        if str(nombre_libro_especifico).isalpha():
            self.libro = nombre_libro_especifico
        else:
            print("El nombre de los libros no es válido")
            self.libro = None

    def mostrar_informacion(self):
        informacion = super().mostrar_informacion()
        return f"{informacion}, Libro especifico: {self.libro}" 

class matematico(estudiante):
    def __init__(self, nombre, num_cuenta, aula, num_materias, materia_especifica):
        super().__init__( nombre, num_cuenta,aula, num_materias,)
        self.especifica= materia_especifica
    def mostrar_informacion(self,):
        informacion= super().mostrar_informacion()
        return f"{informacion}, materia especifica: {self.especifica}"

class electronico(estudiante):
    def __init__(self, nombre, num_cuenta, aula, num_materias, herramientas):
        super().__init__( nombre, num_cuenta, aula, num_materias,)
        self.herramientas= herramientas
    def mostrar_informacion(self,):
        informacion= super().mostrar_informacion()
        return f"{informacion}, herramientas_especificas: {self.herramientas}"

#ejemplo de parametros correctos para crear el objeto denominado "fisico"
estudiante_1 = fisico("Angel Daniel Zazueta Lopez", 20490879, "aula de usos multiples", 5, "Relatividad")
print("La información del primer estudiante es:", estudiante_1.mostrar_informacion())

#paramametros incorrectos al momento de crear el objeto llamado "fisico"
estudiante_2 = fisico("4", "veinte millones cuatrocientos noventa mil ochocientos setenta y nueve", "%", "cinco", 3)
print("La información del segundo estudiante es:", estudiante_2.mostrar_informacion())