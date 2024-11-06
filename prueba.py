

import json

def menu():
    print("""
        ==========================================
        ====== Gestion de Notas Acme School ======
        ==========================================
        =                                        =
        =   1. Registro de usuarios              =
        =   2. Registro de estudiantes           =
        =   3. Creacion de cursos                =
        =   4. Calificar                         =
        =   5. Reporte de calificaciones         =
        =   0. Salir                             =
        =                                        =
        ==========================================
            """)
    opc = input("que desea hacer -->")
    return opc



def login(): 
    usuarios = traerInfo("usuariosDB.json")
    print("===== I N G R E S O =======")
    email = input(">> Ingresa tu correo electronico: ")
    contraseña = input(">> Ingresa contraseña")
    for usuario in usuarios: 
        if contraseña == usuario["contraseña"] and  email == usuario["email"]:
            print("login exitoso")
            return True
    return False

def registro_Usuarios():
    usuarios = traerInfo("usuariosDB.json")
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
    usuarios.append({
        "numero_Identificacion": numero_Identificacion,
        "nombre":nombre,
        "cargo":cargo,
        "email":email_Corporativo,
        "contraseña":contrasenia
    })

    guardarInfo("usuariosDB.json",usuarios)

    print(f"Se registro correctamente al usuario {nombre}")
    return usuarios


def CreacionDB2():
  try:
    file = open("usuariosDB.json", "r")
    file.close()
    return file
  except FileNotFoundError:
    file = open("usuariosDB.json", "w")
    file.write("""[{
       "numero_Identificacion": 12312,
        "nombre": "pepe",
        "cargo": "Administrador",
        "email": "pepe@acme.com",
        "contrase\u00f1a": "asdf" 
    }]""")
    file.close

def traerInfo(archivo,):
  file = open(archivo, "r")
  empleados = json.load(file)
  return empleados

def guardarInfo(archivo,datos):
  file = open(archivo, "w")
  json.dump(datos,file, indent=4)
  file.close()

def creacionEstudiantes():
    estudiantes = traerInfo("estudiantesDB.json")
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

    guardarInfo("estudiantesDB.json",estudiantes)

#....

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
        

