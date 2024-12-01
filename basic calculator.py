number1 = float(input('Enter number1: '))
number2 = float(input('Enter number2: '))
sign = input('Enter operation sign (+, -, *, /): ')

result = None

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

if result is not None:
    print(f'The result of {number1} {sign} {number2} is: {result}')
