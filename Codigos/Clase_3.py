#Condicional

# if 3 > 2:
#     print("3 es mayor que 2")

# print("Hola mundo")

#-------------------------------------------------------#

# variables = 3

# if variables > 3:
#     print("la variable es mayor que 3")
# elif variables <3:
#     print("la variable es menor que 3")
# else:
#     print("la valrible es (3)")

# print("Siempre se muestra")

#-------------------------------------------------------#

# Dinero = 0
# Pesos=""
# Numero= int(input("What conversion do you want to do: \n 1: Argentine pesos to dollars \
#                   \n 2: Colombian pesos to dollars \n 3: Mexican pesos to dollars \n - "))

# if Numero==1:
#     Pesos=("Argentine pesos to dollars")

# elif Numero==2:
#     Pesos=("Colombian pesos to dollars")

# elif Numero==3:
#     Pesos=("Mexican pesos to dollars")

# valor = float(input("Please enter the value of {} that you want to convert to dollars: ".format(Pesos)))

# if Numero==1:
#     Dinero=(valor*0.0029)

# elif Numero==2:
#     Dinero=(valor*0.00025)

# elif Numero==3:
#     Dinero=(valor*0.057)

# else:
#     print("The opcion input is incorrect")

# print("The conversion of {} {} to dollars is: {}".format(valor,Pesos, Dinero))

#-----------------------------------------------------------------------------------------------#

#SOLUCIÓN DEL PROFESOR

# menu= """
# Welcome al changed money

# 1- Pesos Aregentinos
# 2 - Pesos Mexicanos 
# 3- Pesos Colombianos 


# enter your number: """

# opcion = int(input(menu))

# if opcion ==1: 
#     money = float(input ("Enter your money: "))
#     changed = money * 0.0029
#     print ("The value changed is:{}".format(changed))

# elif opcion==2:
#     money1 = float(input ("Enter your money: "))
#     changed1 = money1 * 0.057
#     print ("The value changed is:{}".format(changed1))

# elif opcion==3:
#     money2 = float(input ("Enter your money: "))
#     changed2 = money2 * 0.00025
#     print ("The value changed is:{}".format(changed2))

# else:
#     print("The number is not in the options")

#------------------------------------------------------------------------------------------
