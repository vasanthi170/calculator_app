number1 = input('Enter number1: ')
number2 = input('Enter number2: ')
sign = input('Enter operation sign (+, -, *, /): ')
try:
    number1 = float(number1)
    number2 = float(number2)
    result = 0
    if sign == '+':
        result = number1 + number2
    elif sign == '-':
        result = number1 - number2
    elif sign == '*':
        result = number1 * number2
    elif sign == '/':
        if number2 != 0:
            result = number1 / number2
        else:
            print('Zero Division Error')
    else:
        print('Invalid operation sign!')
        
    print(result)
except:
    print('Invalid number! try again..')

