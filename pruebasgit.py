"Hola esta es la primer modificacion para ver como funciona git"

"se crea una nueva rama y se añadira este cambio en una pull request"

# Información del estudiante
estudiantes = [
    {'nombre':'Maria', 'edad' : 16, 'calificaciones' : [9,8,10]},
]

num_estudiantes = int(input('Cuantos estudiantes agregaras: '))
#Definimos que solo tenemos 3 materias o calificaciones por materia
num_calificaciones = 3

def agregaralumnos():
    for i in range(num_estudiantes):
        n = 1
        nombre = input('\nIngrese el nombre del estudiante: ')
        edad = input('Ingrese la edad del estudiante: ')
        calificaciones = []

        for i in range (num_calificaciones):
            calificacion = float(input(f'Ingrese la calificacion del estudiante:{n}- '))
            calificaciones.append(calificacion)
            n += 1
        estudiante = {'nombre': nombre , 'edad' : edad, 'calificaciones' : calificaciones}
        estudiantes.append(estudiante)

# Función para mostrar la información del estudiante
def mostrar_informacion_estudiante(estudiantes):
    for estudiante in estudiantes:
        print("Nombre:", estudiante.get('nombre'))
        print("Edad:", estudiante.get('edad'))
        print(f"Calificaciones:", estudiante.get('calificaciones'))
        calcular_promedio(estudiante.get('calificaciones'))
        print()

# Función para calcular el promedio de calificaciones
def calcular_promedio(califs):
        total = sum(califs)
        cantidad = len(califs)
        print('Promedio:',total / cantidad)

# Uso de las funciones
agregaralumnos()
mostrar_informacion_estudiante(estudiantes)
