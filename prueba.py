estudiantes ={}



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

            except ValueError:
                print("Error.. vuelve a intentar ")

def reporte():
    print("==== R E P O R T E  D E  N O T A S =====")


while True:
    creacion_curso()