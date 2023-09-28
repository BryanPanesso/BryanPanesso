social_stratum=0
consumption_value=0
invoice_value=0


social_stratum= int(input("Enter the stratum: "))
consumption_value=float(input("Enter the consumption value: "))

if social_stratum==1:
   invoice_value= consumption_value+500

elif social_stratum==2:
    invoice_value= consumption_value+700

elif social_stratum==3:
   invoice_value= consumption_value+4800

elif social_stratum==4:
    invoice_value= consumption_value+6700

else:
    print("The category is not valid")

internet=(invoice_value/100)*20
cleanliness=(invoice_value/100)*12.2
invoice_value=invoice_value+internet+cleanliness

print("The total value to be paid for the invoice is: ", invoice_value)

