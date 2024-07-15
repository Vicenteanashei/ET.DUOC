from os import system
system("cls")
import statistics
import random

trabajadores = {1: ["Juan Perez"],2: ["Maria Garcia"],3: ["Carlos Lopez"],4: ["Ana Martinez"],5: ["Pedro Rodriguez"],6: ["Laura Hernandez"],7: ["Miguel Sanchez"],8: ["Isabel Gomez"],9: ["Francisco Diaz"],10: ["Elena Fernandez"],11: ["Profe no me acuerdo"]}
trabajadores_sueldos= []
def asignar_sueldos():
    system("cls")
    for i, asignar in trabajadores.items():
        sueldo=random.randint(300000, 2500000)
        print(f"Sueldo {asignar}: {sueldo}")
        trabajadores_sueldos.append(sueldo)
           
        
def clasificar_sueldos():
    system("cls")
    for sueldos in trabajadores_sueldos:
        if sueldos<800000:
            print("SUELDO MENOR A $800.000")
            print(f"""
NOMBRE EMPLEADO          SUELDO
{trabajadores[11]}           ${sueldos}
""")
    for sueldos in trabajadores_sueldos:
        if sueldos >800000 and sueldos <2000000:
            print("SUELDO ENTRE $800.000 Y $2.000.000")
            print(f"""
NOMBRE EMPLEADO          SUELDO
{trabajadores[11]}           ${sueldos}
""")
    for sueldos in trabajadores_sueldos:
        if sueldos >2000000:
            print("MAYOR A $2.000.000")
            print(f"""
NOMBRE EMPLEADO          SUELDO
{trabajadores[11]}           ${sueldos}
""")

def ver_estadisticas():
    system("cls")
    for buscar in trabajadores_sueldos:
        if buscar>buscar:
            print(f"El sueldo menor es: {buscar}")
    for buscar in trabajadores_sueldos:
        if buscar<buscar:
            print(f"El sueldo mas alto es: {buscar}")
    

def reporte_sueldos():
    des_salud=trabajadores_sueldos*0.07
    des_afp=trabajadores_sueldos*0.12
    sueldo_liquido=sueldo_liquido-des_salud-des_afp
    archivo=open("Reporte.csv", "w")
    archivo.write("Nombre_Empleado,Sueldo_Base,Descuento_Salud,Descuento_AFP,Sueldo_Liquido")
    for i in trabajadores:
        trabajadores_sueldos=float(trabajadores_sueldos)
        des_salud=trabajadores_sueldos*0.07
        des_afp=trabajadores_sueldos*0.12
        sueldo_liquido=sueldo_liquido-des_salud-des_afp
        print(f"{trabajadores}{trabajadores_sueldos},{des_salud},{des_afp},{sueldo_liquido}")
    archivo.close
     
while True:
    op = input("""
1.Asignar sueldos
2.Clasificar sueldos
3.Ver estadisticas
4.Reporte de sueldos
5.Salir del programa
               
""")
    match op:
        case "1":
            asignar_sueldos()
        case "2":
            clasificar_sueldos()
        case "3":
            ver_estadisticas()
        case "4":
            reporte_sueldos()
        case "5":
            break



https://github.com/Vicenteanashei/ET.DUOC