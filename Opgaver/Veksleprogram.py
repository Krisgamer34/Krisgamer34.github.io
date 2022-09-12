
print('How many ddk would you like to convert? Please write a number as ')
Krone_amount = float(input())
Krone_to_euro = 0.13    
Vekslet = float(Krone_amount * Krone_to_euro)
kommision = float(Vekslet / 50)
if float(Vekslet / 50) <= 0.5:
    print('Your amount is ' + str(Vekslet - 0.5))
else: 
    print('Your amount is ' + str(Vekslet - kommision))

    