def factorial(n):
  
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

number = int(input("Enter a non-negative integer: "))

if number < 0:
  print("Invalid input: Number must be non-negative.")
else:
  factorial_result = factorial(number)
  print(f"The factorial of {number} is: {factorial_result}")
