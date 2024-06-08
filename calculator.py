class Calculator:
  def add(self, a, b):
    return a + b

  def subtract(self, a, b):
    return a - b

  def multiply(self, a, b):
    return a * b

  def divide(self, a, b):
    if b == 0:
      raise ValueError("Cannot divide by zero!")
    return a / b

  def power(self, a, b):
    return a ** b
  
  def factorial(self, a):
    if a == 0:
      return 1
    return a * self.factorial(a-1)
  
  def fibonacci(self, a):
    if a == 0:
      return 0
    if a == 1:
      return 1
    return self.fibonacci(a-1) + self.fibonacci(a-2)
  
  def is_prime(self, a):
    if a <= 1:
      return False
    for i in range(2, a):
      if a % i == 0:
        return False
    return True
