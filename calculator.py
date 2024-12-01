def select(number):
    while True:
        try:
            return float((input('Enter number' + str(number)+':')))
            break
        except:
            print('Invalid number! try again..')
number1 = select(1)
number2 = select(2)
sign = input('Enter operation sign (+, -, *, /): ')
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
        
print(f'The result is: {result}')

