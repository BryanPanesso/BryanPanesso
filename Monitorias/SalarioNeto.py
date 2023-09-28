# cedula = int(input("Ingrese el numero de cedula: "))
# salariobasico = int(input("Ingrese el salario basico: "))
# anoVinculacion = int(input("Ingrese el año vinculacion: "))

# if (salariobasico> 1200000) and (anoVinculacion >1995):
#     salarioneto= salariobasico - ((salariobasico/100)*6)
# elif(salariobasico< 550000) or (anoVinculacion==1995):
#     salarioneto=salariobasico- ((salariobasico/100)*3)
# else: salarioneto=salariobasico - ((salariobasico/100)*4)
    
# print("El usuario con numero de cedula: {} tiene un salario neto de: {}".format(cedula, salarioneto))




# cedula= str(input("Por favor ingrese el número de cedula: "))
# año=int(input(" Por favor ingrese el año de vinculación en la empresa: "))
# ganancia=int(input(" Por favor ingrese la ganancia al mes: "))

# if (ganancia>1200000) and (año>1995):
#     print(f"Su cedula es {cedula} y su sueldo neto es de {((ganancia+(ganancia*6/100)-(ganancia*4/100)))}")
# elif (ganancia<550000) or (año==1995):
#     print(f"Su cedula es {cedula} y sueldo neto es de {((ganancia+(ganancia*3/100)-(ganancia*4/100)))}")
# else:
#     print(f"Su cedula es {cedula} y sueldo neto es de {((ganancia+(ganancia*4/100)-(ganancia*4/100)))}")



edad = int(input("Ingrese su edad: "))

if(edad<0)or(edad>120):
    print("Edad invalida") 
elif(edad>=0)and(edad<10):
    print("Vaya a la niñiteca")
elif(edad>=10)and(edad<15):
    print("Vaya a la chiquiteca")
elif(edad>=15)and(edad<=17):
    print("Vaya a la casa")
elif(edad>=18)and(edad<25):
    print("Vaya a la seccion jovenes")
elif(edad>=25)and(edad<=35):
    print("Vaya a la seccion adultos jovenes")
elif(edad>35)and(edad<65):
    print("Vaya a la seccion maduros")
elif(edad>=65)and(edad<80):
    print("Vaya a la seccion de viejoteca")
elif(edad>=80):
    print("Vaya a la seccion vip")