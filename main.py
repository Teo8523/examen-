from estudiantes import CreacionDB,creacionEstudiantes,traerInfo,guardarInfo
from prueba import registro_Usuarios, menu,CreacionDB2,login

CreacionDB()
CreacionDB2()

while True:
    ingreso = login()
    if ingreso == False:
        print("intente de nuevo")
    if ingreso:
        repuesta = menu()

        match repuesta:
            case "1":
                registro_Usuarios()
            case "2":
                 creacionEstudiantes()


       