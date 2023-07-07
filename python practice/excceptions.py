import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: enter an integer")
    sys.exit(1)

try:
    div = x/y
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    sys.exit(1)
    
print(f"{x} / {y} = {div}")