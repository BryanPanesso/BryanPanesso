"""
Entrada: 

"""
dato1 = int(input("Ingrese el primer dato: "))
dato2 = int(input("Ingrese el segundo dato: "))

dato3= int(input("Que operacion deseas realizar: \n 1.Suma \n 2.Resta \n 3.Multiplicar \n 4. Dividir "))

if dato3==1:
    dato= dato1 + dato2
elif dato3==2:
    dato= dato1 - dato2 
elif dato3==3:
    dato= dato1 * dato2      
elif dato3==4:
    dato= dato1 / dato2
else: dato=0

print(dato)