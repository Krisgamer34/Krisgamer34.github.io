while(True):
    talStr = input ('Hvilke tal? (Separer med mellemrum)')
    tal = []
    try:
        talStr = talStr.split()
    except:
        continue
    try:
        for i in talStr:
            i = float(i)
            tal.append(i)
    except:
        print('Nogle værdier er ikke korrket, prøv igen')
        continue
    else:
        break

#sætter listen til at starte i 0(den første) og sætte loopet til at stoppe ved største tal. sætter største tal som n 
largestNumber=tal[0]
for n in tal:
    if(n > largestNumber):
        largestNumber = n
#det samme som largest men med mindste
smallestNumber = tal[0]
for n in tal:
    if(n < smallestNumber):
        smallestNumber = n

print(f'Det største tal er {largestNumber} og det mindste tal er {smallestNumber}')
    #Tak Henrik for at lade mig kopiere