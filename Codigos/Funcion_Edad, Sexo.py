
def run():
    pass

def saluditos(nombre,sexo):
    print("Hello " + nombre)

    if sexo=="M":
        print("comfirmado, eres sexo hombre")
    
    elif sexo=="F":
        print("comfirmado, eres sexo mujer")

    elif sexo== "NB":
        print("comfirmado, eres sexo no binarie")
    
    else:
        print("como te va ve....")
    
def definiredad(age):
    
    if age<0 or age>120:
        print("Enter a valid age")
    
    elif age<18:
        print("You are a minor")
    
    elif age>=18:
        print("You're of age")

    else:
        print("Please enter a number")
        

if __name__ == "__main__":
    run()
    name = input("Enter your name: ").upper()           #.upper() para convertir todo en mayusculas
    gender = input("Enter your gender: (M), (F), (NB): ").upper()
    age = int(input("Enter your age: "))
    saluditos(name,gender)
    definiredad(age)