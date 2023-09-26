def factorial(numero):
    if numero == 1: 
        return 1
    else:
        return numero * factorial(numero-1)
    
def MultiplicacionExpresion(numero):

    if numero == 1:
        return "1"
    
    else:
        return f"{MultiplicacionExpresion (numero - 1)}"
    

#------------------------------------------------------------

def ConvertirBinario(numero):
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    else:
        return ConvertirBinario(numero//2) + str(numero%2)
    
print(ConvertirBinario(35))