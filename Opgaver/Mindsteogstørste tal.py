


print('Welcome to the bigger better and harder sorter. its veiny too')
print('Please enter your first number')
number1 = input()

print('Please enter your second number')
number2 = input()

print('Please enter your third number')
number3 = input()

if float(number1) > float(number2) and float(number1)> float(number3):
    print('The biggest number is ' + str(number1))
elif float(number2) > float(number1) and float(number2) > float(number3):
    print('The biggest number is ' + str(number2))
elif float(number3) > float(number2) and float(number3) > float(number1):
    print('The biggest number is ' + str(number3))
elif float(number1) == float(number2) and float(number1) == float(number3) and float(number2) == float(number3):
    print('They are all the biggest')
elif float(number1) == number2 and float(number1) > float(number3):
    print(number1 +'and ' + number2 + ' is the biggest' )
elif float(number1) == number3 and float(number1) > float(number2):
    print(number1 + 'and '+ number3 +' is the biggest')
elif float(number2) == number3 and float(number2) > float(number1):
    print(number2 +'and'+ number3 + ' is the biggest')

if float(number1) < float(number2) and float(number1)< float(number3):
    print('The smallest number is ' + str(number1))
elif float(number2) < float(number1) and float(number2) < float(number3):
    print('The smallest number is ' + str(number2))
elif float(number3) < float(number2) and float(number3) < float(number1):
    print('The smallest number is ' + str(number3))
elif float(number1) == float(number2) and float(number1) == float(number3) and float(number2) == float(number3):
    print('They are all the same')
elif float(number1) == number2 and float(number1) < float(number3):
    print(str(number1) +'and ' + str(number2) + ' is the smallest' )
elif float(number1) == number3 and float(number1) < float(number2):
    print(str(number1) + 'and '+ str(number3) +' is the smallest')
elif float(number2) == number3 and float(number2) < float(number1):
    print(str(number2) +'and'+ str(number3) + ' is the smallest')


