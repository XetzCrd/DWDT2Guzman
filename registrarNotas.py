
#<=========================== FUNCIONES ===========================>#
def menu():
    print("\n\n====================================================")
    print("Seleccione un comando:")
    print("R: Registrar alumnos")
    print("C: Calificar alumnos")
    print("P: Obtener el promedio de todos los alumnos registrados")
    print("S: Obtener la suma de todos los alumnos registrados")
    print("X: Salir de la aplicación")
    print("====================================================", end="\n\n")

#<=========================== CÓDIGO ===========================>#
if __name__=='__main__':
    from alumnos import alumnos

    alumnosList = []
    cmds = ["R","C","P","S","X"]

    print()
    print("Bienvenidos al registro de notas")

    while True: 
        menu()  
        cmd = input("Ingrese un comando: ").upper() 

        if cmd in cmds:

        #R: REGISTRAR ALUMNOS
            if cmd == "R":
                while True:
                    cant = "0"
                    while (cant.isnumeric() == True and int(cant) > 0) == False:
                        cant = input("Cantidad de alumnos a registrar: ")

                    for i in range(int(cant)):
                        print("Ingrese los datos del alumno",i+1,":")
                        alumno = alumnos(
                            nombre = input("Nombre: "),
                            apellido = input("Apellido: "),
                            edad = input("Edad: "),
                            nacionalidad = input("Nacionalidad: "),
                        )  
                        alumno.getAlumno()
                        alumnosList.append(alumno)

                    if input("¿Desea registrar más alumnos? (*/N): ").upper() == "N":
                        break

        #C: CALIFICAR ALUMNOS
            if cmd == "C":                
                for i in alumnosList:
                    nota = input(f"{i.id}. Alumno {i.getAlumno()}, ingrese nota: ")

                    while (nota.isnumeric() == True and int(nota) <= 20 and int(nota) >= 0) == False:
                        nota = input(f"{i.id}. Alumno {i.getAlumno()}, ingrese nota: ")
                    
                    i.registrarNota(int(nota))

                if(alumnos.obtener_contador() < 1): 
                    print("No hay alumnos registrados")
                else:
                    print("Se realizó la calificación a los alumnos")    

        #P: PROMEDIAR NOTAS
            if cmd == "P":
                promedio = 0
                for i in alumnosList:
                    promedio += i.leerNota()/alumnos.obtener_contador()

                if(alumnos.obtener_contador() < 1): 
                    print("No hay alumnos registrados")
                else:
                    print(f"El promedio de notas para {alumnos.obtener_contador()} alumnos es: {promedio:.2f}")   

        #S: SUMAR NOTAS
            if cmd == "S":
                suma = 0
                for i in alumnosList:
                    suma += i.leerNota()

                if(alumnos.obtener_contador() < 1): 
                    print("No hay alumnos registrados")
                else:
                    print(f"La suma de notas de {alumnos.obtener_contador()} alumnos es: {suma:.2f}")   

        #X: SALIR
            elif cmd == "X":
                print("\n\nRegistro de notas cerrado",end="\n\n")
                break
    
        #OTRO: PREGUNTAR DE NUEVO
        else:
            print("El comando ingresado es incorrecto")                

