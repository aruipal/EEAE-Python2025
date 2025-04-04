'''Crea una clase Estudiante con atributos para nombre, edad y calificación.
Implementa métodos getter y setter, y un método que determine si el estudiante 
aprobó (calificación mayor o igual a 6).'''

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
   
    def set_calificacion(self,calificacion):
        self.calificacion = calificacion

    def get_calificacion(self):
        return self.calificacion
    
    def notas(self):
        try:
            self.calificacion = float(input("Introduzca la nota: "))
            if self.calificacion >= 6:
                return (self.nombre, "está aprobado.")
            else:
                return (self.nombre, "está suspenso.")
        except ValueError:
            return "Introduzca un valor numérico."
            self.notas()
 
estudiante1 = Estudiante("Antonio",23)
print(estudiante1.notas())