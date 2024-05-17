class ArithmeticOperation:

 def __init__(self, operation_type):

  self.operation_type = operation_type

def operation(self, a, b):

 if self.operation_type == '+':

  return self._addition(a, b)

 elif self.operation_type == '-':

  return self._subtraction(a, b)

 elif self.operation_type == '*':

  return self._multiplication(a, b)

 elif self.operation_type == '/':

  return self._division(a, b)

 else:

  return f"Operation '{self.operation_type}' has not been implemented."

def _addition(self, a, b):

 return self._convert_to_float(a) + self._convert_to_float(b)

def _subtraction(self, a, b):

 return self._convert_to_float(a) - self._convert_to_float(b)

def _multiplication(self, a, b):

 return self._convert_to_float(a) * self._convert_to_float(b)

def _division(self, a, b):

 if self._convert_to_float(b) == 0:

  return "Division by zero is not possible."

  return self._convert_to_float(a) / self._convert_to_float(b)

def _convert_to_float(self, number):

 try:

  return float(number)

 except ValueError:

  return 0.0

# Використання класу для виконання операцій

arith_op = ArithmeticOperation('+')

value1 = 2

value2 = 5

result = arith_op.operation(value1, value2)

print(result)

arith_op = ArithmeticOperation('/')

result = arith_op.operation(value1, value2)

print(result)

