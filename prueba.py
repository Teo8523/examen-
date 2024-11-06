estudiantes ={}

import json

def menu():
    print("""
        ==========================================
        ====== Gestion de Notas Acme School ======
        ==========================================
        =                                        =
        =   1. Login                             =
        =   2. Registro de usuarios              =
        =   3. Registro de estudiantes           =
        =   4. Creacion de cursos                =
        =   5. Calificar                         =
        =   6. Reporte de calificaciones         =
        =   0. Salir                             =
        =                                        =
        ==========================================
            """)



def registro_Usuarios(usuarios):
    numero_Identificacion = int(input("Ingrese su numero de identificacion"))
    nombre = input("Ingrese su nombre")
    try:
        cargo = input("""Segun su cargo coloque la opcion correcta
                                --> Administrador
                                --> Profesor
                        """)
    except ValueError:
        print("Ingrese un cargo valido")
        return
    email_Corporativo = input("Ingrese su correo corporativo")
    contrasenia = str(input("Ingrese su contraseña"))

    #if numero_Identificacion not in usuarios:
    #usuarios[numero_Identificacion] = {
    # "nombre":nombre,
    # "cargo":cargo,
    # "email":email_Corporativo,
    # "contraseña":contrasenia,
    # }

    print(f"Se registro correctamente al usuario {nombre}")
    return usuarios

    # else:
        #print("El usuario ya se encuentra registrado")
        #return usuarios

def CreacionDB():
  try:
    file = open("estudiantesDB.json", "r")
    file.close
    return file
  except FileNotFoundError:
    file = open("estudiantesDB.json", "w")
    file.write("""[{
        
    }]""")
    file.close

def traerInfo():
  file = open("estudiantesDB.json", "r")
  empleados = json.load(file)
  return empleados

def guardarInfo(datos):
  file = open("estudiantesDB.json", "w")
  json.dump(datos,file, indent=4)
  file.close()

def creacionEstudiantes():
    estudiantes = traerInfo()
    try:
        numeroDeIndentificacion = int(input("ingrese el numero de indentificacion del estudiante -->"))
    except ValueError:
       print("el numero de identificacion debe ser un numero")
       return
    nombre = input("ingrese el nombre del estudiante -->")
    apellido = input("ingrese el apellido del estudiante -->")
    email = input("ingrese el email del estudiante -->")
    fechaDeNacimiento = input("ingrese el fecha de nacimiento del estudiante -->")
    estudiantes.append({
        "numeroDeIndentificacion": numeroDeIndentificacion,
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "fechaDeNacimiento": fechaDeNacimiento,
    })

    guardarInfo(estudiantes)

#....

CreacionDB()

creacionEstudiantes()
def inscripcion():
     if estudiante in estudiantes:
          curso[estudiantes].append(estudiante)
          print(f"el estududiante a sido agregado al curso")

def creacion_curso():
            print("======== C R E A C I O N  C U R S O  A C M E ========")
            try:
                codigo = int(input(">> Ingresa el codigo del curso: "))
                if codigo not in estudiantes:
                    nombre_curso = input(">> Ingresa el nombre del curso: ")
                    descrip = input(">> Ingresa  la descripcion: ")

                    estudiantes[codigo] ={
                        "Codigo": codigo,
                        "Curso": nombre_curso,
                        "descripcion": descrip
                    }

                    print("==== I N F O R M A C I O N ==")
                    print("Codigo:", codigo)
                    print("Curso:" , nombre_curso)
                    print("Descripcion:", descrip )
                    print("-- C U R S O  R E G I S T R A D O ---")
                else:
                    print("El codigo del curso ya se encuentra registrado...")

                    # ingreso = input("--Quieres ingresar un estudiante: S/N")
                    # if ingreso == "S":
                        


            except ValueError:
                print("Error.. vuelve a intentar  ")

def reporte():
    if estudiantes:
         print("==== R E P O R T E  D E  N O T A S =====")
        

while True:
    creacion_curso()