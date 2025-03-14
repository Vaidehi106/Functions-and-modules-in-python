import math
try:
  num=int(input("enter a number: "))

  root=math.sqrt(num)
  print("square root: ",root)

  log=math.log(num)
  print("natural logarithm (base e): ",log)

  sine=math.sin(num)
  print("sine(radians): ",sine)

except  ValueError:
    print("Invalid input. Please enter a non-negative number.")
except Exception as e:
    print(f"An error occurred: {e}")

