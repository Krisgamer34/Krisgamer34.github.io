print('Please input the weight of your letter')
Weight = input()
price100 = '29kr'
price250 = '58kr'
price2000 = '87kr'

if float(Weight) <= 100:
    print('It will cost ' + price100 + ' to send this letter')
elif float(Weight) <=250:
    print('It will cost ' + price250 + ' to send this letter')
elif float(Weight) <= 2000:
    print('It will cost ' + price2000 + ' to send this letter')
else:
    print('This letter weighs too much to be sent as a letter. We ask you send it as a package. This will also cost more. We apologize for the inconvience')