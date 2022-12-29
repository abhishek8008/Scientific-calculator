import math

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

def mod(x, y):
  return x % y

def square_root(x):
  return math.sqrt(x)

def exponent(x, y):
  return x ** y

def sin(x):
  return math.sin(x)

def cos(x):
  return math.cos(x)

def tan(x):
  return math.tan(x)

def rad_to_deg(x):
  return x * (180 / math.pi)

def deg_to_rad(x):
  return x * (math.pi / 180)

while True:
  print("Enter the operation you would like to perform:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Modulo")
  print("6. Square root")
  print("7. Exponent")
  print("8. Sine")
  print("9. Cosine")
  print("10. Tangent")
  print("11. Convert radians to degrees")
  print("12. Convert degrees to radians")
  print("13. Exit")

  choice = int(input())

  if choice == 13:
    break

  if choice in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
    x = float(input("Enter the first number: "))
    if choice in [1, 2, 3, 4, 5]:
      y = float(input("Enter the second number: "))

  if choice == 1:
    result = add(x, y)
  elif choice == 2:
    result = subtract(x, y)
  elif choice == 3:
    result = multiply(x, y)
  elif choice == 4:
    result = divide(x, y)
  elif choice == 5:
    result = mod(x, y)
  elif choice == 6:
    result = square_root(x)
  elif choice == 7:
    result = exponent(x, y)
  elif choice == 8:
    result = sin(x)
  elif choice == 9:
    result = cos(x)
  elif choice == 10:
    result = tan(x)
  elif choice == 11:
    result = rad_to_deg(x)
  elif choice == 12:
    result = deg_to_rad(x)

  print("The result is:", result)
