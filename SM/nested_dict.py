car = {1: {'number1': 1234, 'value1': 123},
       2: {'number2': 9432, 'value2': 432},
        }

number = 'number'+str(3)
value = 'value'+str(3)
num = int(input('Enter the number: '))
val = int(input('Enter the value: '))
car[3] = {number: num, value: val}

for key in car.keys():
    print(key, ' = ', car[key])
