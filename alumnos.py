#Clase alumnos
class alumnos:
    contador = 0

    def __init__(self,nombre,apellido,edad,nacionalidad,nota="No registrada"):
#VARIABLES
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nota = nota
        self.nacionalidad = nacionalidad

        alumnos.contador += 1 #Actualizar la cantidad de alumnos actual
        self.id = alumnos.contador 

#MÉTODOS
    def getAlumno(self):
        return f"{self.nombre} {self.apellido}"
    
    def leerNota(self):
        return self.nota
    
    def registrarNota(self, nota):
        self.nota = nota
        return ">> Se ha registrado la nota de {self.nota} para {self.nombre} {self.apellido}"

    @staticmethod
    def obtener_contador():
        return alumnos.contador
    

#a = alumnos("Yomira", "Guzman", "27", "20", "Peruana")

#a.getAlumno()
#a.leerNota()

#print(alumnos.obtener_contador())