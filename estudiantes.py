import json

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






