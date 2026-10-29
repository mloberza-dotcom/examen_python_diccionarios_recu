notas={
    "maldonado":[],
    "moyano":[],
    "perez":[],
    "almada":[],
    "salatic":[]
 }
suma=0
while True:
    opcion=int(input(" 1. Ver todas las notas \n 2. Ver un alumno en especifico\n 3. Cargar notas \n 4. Promedio de un alumno especifico\n"))
    if opcion==1:
        for k,n in notas.items():
            print(f"{k} {n}")
    if opcion==2:
        alumno=input("De quien queres saber las notas \n")
        valores=notas[alumno]
        for i in range(5):
            print(valores[i])
    if opcion==3:
        alumno=input("De quien queres cargar las notas \n")
        valores=notas[alumno]
        for i in range (5):
            notardas=int(input("Carga tu nota \n"))
            if notardas <11 and notardas>0:
                suma=suma+notardas
                valores.append(notardas)
            else:
                print("Del 1 al 10 las notas")
    if opcion==4:
        alumno=input("De quien queres saber el promedio \n")
        valores=notas[alumno]
        prom=suma/len(valores)
        print(prom)
