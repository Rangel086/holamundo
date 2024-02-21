# Definición de la clase Alumnos
class Alumnos:
    # Método inicializador
    def __init__(self, matricula, nombre):
        # Asignación de la matrícula
        self.matricula = matricula
        # Asignación del nombre
        self.nombre = nombre

# Creación de un objeto de la clase Alumnos
objetoAlumnos = Alumnos('matricula', 'nombre')  # Se crea un alumno con matrícula 'matricula' y nombre 'nombre'

# Impresión del nombre del objeto
print(objetoAlumnos.nombre)  # Se imprime el nombre del alumno, que es 'nombre'
