MyList = [1,2,3,4,5]
division = -1
a = 10
b = 3



try:
   division = a / b
   print(f'{a} / {b} = {division}')
except(Exception) as error:
    print(error)
#except (TypeError) as error:
#   print(error)

finally:
    MyList.append(division)

for value in MyList:
    print(value)

class Calculator:

   def __init__(self):

       pass

   @staticmethod

   def convert_to_float(value):

       try:

           return float(value)

       except ValueError:

           print("Could not convert the input to float.")

           return None

       finally:

           print("Conversion attempted.")

   @staticmethod

   def add(a, b):

       return a + b

   @staticmethod

   def subtract(a, b):

       return a - b

   @staticmethod

   def multiply(a, b):

       return a * b

   @staticmethod

   def divide(a, b):

       try:

           result = a / b

           return result

       except ZeroDivisionError:

           print("Cannot divide by zero.")

           return None

       finally:

           print("Division attempted.")

# Приклад використання класу Calculator

calc = Calculator()

# Конвертація типу даних str в float

str_value = "3.14"

float_value = calc.convert_to_float(str_value)

print(float_value)

# Додавання

result_addition = calc.add(5, 3)

print("Addition:", result_addition)

# Віднімання

result_subtraction = calc.subtract(10, 4)

print("Subtraction:", result_subtraction)

# Множення

result_multiplication = calc.multiply(6, 7)

print("Multiplication:", result_multiplication)

# Ділення з обробкою винятків

result_division = calc.divide(8, 2)

print("Division:", result_division)

# Ділення на нуль (викличе обробку винятку)

result_division_by_zero = calc.divide(10, 0)

print("Division by zero result:", result_division_by_zero)

