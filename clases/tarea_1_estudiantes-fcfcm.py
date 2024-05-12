#crear una clase padre donde se representen las caracteristicas generales de un alumno de la fcfm, para posteriormente ramificarse en tres clases secundarias,(fisica, matematicas, electronica). 
class estudiante():
    def __init__(self, nombre, num_cuenta, aula, num_materias):
        self.nombre= nombre
        self.num_cuenta= num_cuenta 
        self.num_aula= aula
        self.num_materias= num_materias
    def mostrar_informacion(self):
        return f"nombre del alumno: {self.nombre}, numero de cuenta: {self.num_cuenta}, numero de aula: {self.num_aula}, cantidad de materias: {self.num_materias}"

class fisico(estudiante):
    def __init__(self, nombre, num_cuenta, aula, num_materias, libros):
        super().__init__( nombre, num_cuenta, aula, num_materias,)
        self.libros= libros
    def mostrar_informacion(self,):
        informacion= super().mostrar_informacion()
        return f"{informacion}, libros: {self.libros}" 

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

#ejemplo de algunos estudiantes especificos de cada licenciatura
estudiante_1= matematico("lucas", "20490870", 2, 5, "matematicas discretas")
estudiante_2= electronico("felipe", "20480723", 3, 6, "multimetro, cautín")
estudiante_3= fisico("antonio", "20490875", 1, 5, "relatividad general, mecanica estadistica aplicada")

#imprimimos la informacion de los estudiantes registrados en la facultad
print("la informacion del estudiante #1 es: ", estudiante_1.mostrar_informacion())
print("la informacion del estudiante #2 es: ", estudiante_2.mostrar_informacion())
print("la informacion del estudiante #3 es: ", estudiante_3.mostrar_informacion())
