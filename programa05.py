# Definición de la clase Alumno
class Alumno:
    # Constructor de la clase Alumno
    def __init__(self, matricula, nombre):
        # Atributo matricula de la clase Alumno
        self.matricula = matricula
        # Atributo nombre de la clase Alumno
        self.nombre = nombre
        print("objeto Alumno creado")  # Mensaje de consola

    # Método de la clase Alumno
    def estudiar(self):
        print(f"{self.nombre} estudia")  # Mensaje de consola

    # Método de la clase Alumno
    def sumar(self, numero1, numero2):
        suma = numero1 + numero2  # Variable suma
        print(f"{numero1} + {numero2} = {suma}")  # Mensaje de consola

# Creación de objeto de la clase Alumno
dejah = Alumno(111, "dejah")  # Se crea un alumno con matrícula 111 y nombre 'dejah'
dejah.estudiar()  # Llamada al método estudiar del objeto de la clase Alumno
dejah.sumar(10,5)  # Llamada al método sumar del objeto de la clase Alumno
