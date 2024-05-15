import logging

class Calculation:

def __init__(self):

logging.basicConfig(level=logging.DEBUG,

filename='kjhgfrtyhjk.log',

filemode='a',

format='LOG DATA: %(asctime)s - %(levelname)s - %(message)s',)

def __call__(self, operation, a, b):

result = None

flag = False

try:

if operation == '+':

result = a + b

elif operation == '-':

result = a - b

elif operation == '*':

result = a * b

elif operation == '/':

result = a / b

else:

raise ValueError("Invalid operation")

except Exception as ex:

flag = True

logging.exception(ex)

finally:

if flag:

print(f'Error occurred while performing {operation} operation with {a} and {b}')

else:

print(f'{a} {operation} {b} = {result}')

def check_and_convert(self, data):

try:

converted_data = int(data)

print(f"Successfully converted {data} to int: {converted_data}")

return converted_data

except ValueError as ex:

try:

converted_data = float(data)

print(f"Successfully converted {data} to float: {converted_data}")

return converted_data

except ValueError as ex:

logging.exception(ex)

print(f"Error occurred while converting {data} to int or float")

calc = Calculation()

calc('+', 5, 2)

calc('-', '5', 2)

calc.check_and_convert('10')

calc.check_and_convert('10.5')

calc.check_and_convert('abc')