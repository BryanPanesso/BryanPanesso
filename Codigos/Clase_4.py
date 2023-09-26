#funtion
# import random #importa la libreria aleatoria
# from random import * #para importar todas las caracteristicas

# def square(a):

#     return a * a


# if __name__ == "__main__":

#     number = randint(0,20)
#     x = square(number)
#     print("The values of funtions square is: {}".format(x))

#______________________________________________________________________________________________#

#variables locales y globales

# global variable
# variable = "Estoy afuera de la funcion"#vaiable global

# def una_funcion():
#     variable="Estoy dentro de la funcion"#vaiable local
#     print(variable)

# if __name__ == "__main__":

#     una_funcion()
#     print(variable)

#______________________________________________________________________________________________#

# global var
# var = 3

# def test_global(x):
#     return x * var

# def mult(x):
#     var = 5
#     return x * var

# def multip(x):
#     var = 7
#     return x * 7


# if __name__ == "__main__":
    
#     print(test_global(6))
#     print(mult(6))
#     print(multip(2))

#______________________________________________________________________________________________#


# square =lambda x: x + x
# square2 =lambda x,y: x + y

# print(square(2,3))
# print(square2(2))


#______________________________________________________________________________________________#


# def test_p(age_2, a= 3):
#     if age_2>= 18:
#         #print(a)
#         return True
#     else: 
#         return False

# if __name__ == "__main__":
#     age = int(input("Enter your age: "))
#     test_p(age,a=2)

def test_p(age_2):
    if age_2>= 18:
        return True
    else: 
        return False

if __name__ == "__main__":
    age = int(input("Enter your age: "))
    x=test_p(age)
    if x:
        print("eres mayor de edad")
    else:
        print("Eres menor de edad") 

