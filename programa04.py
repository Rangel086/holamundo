# Definimos la clase Alumnos
class Alumnos:
    # atributo matricula
    matricula = None
    # atributo nombre
    nombre= None

    # definimos el metodo init
    def __init__(self, matricula, nombre):
        # asignamos a la variable matricula el valor que se le pasa como parametro
        self.matricula = matricula
        # asignamos a la variable nombre
        self.nombre = nombre
        print("objeto Alumnos")  # imprimimos el mensaje objeto Alumnos

# creamos un objeto de la clase Alumnos
objetoAlumno = Alumnos(111, "Dejah")
# creamos un objeto de la clase Alumnos
objetoAlumno2 = Alumnos(222, "jhon")
