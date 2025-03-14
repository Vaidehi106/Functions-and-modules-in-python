# Calculate Factorial Using a Function 
1.  **`factorial(n)` Function:**
    * **Purpose:** This function calculates the factorial of a given integer `n`.
    * **Input:** It takes one integer argument, `n`.
    * **Initialization:** A variable `product` is initialized to 1. This variable will store the calculated factorial.
    * **Looping:** A `for` loop iterates through the range of numbers from 1 up to and including `n`.
    * **Calculation:** In each iteration, the current number `i` is multiplied with the `product`. This accumulates the product of all numbers from 1 to `n`.
    * **Return Value:** The function returns the final calculated `product`, which is the factorial of `n`.

2.  **User Input:**
    * The script prompts the user to "enter a number:" using the `input()` function.
    * The input, which is initially a string, is converted to an integer using the `int()` function and stored in the variable `var`.

3.  **Function Call:**
    * The `factorial()` function is called with the user-provided integer `var` as an argument.
    * The returned value (the factorial of `var`) is stored in the variable `result`.

4.  **Output:**
    * The calculated factorial, stored in the `result` variable, is printed to the console using the `print()` function.

# Using the Math Module for Calculations
1.  **Import `math` Module:**
    * `import math`: Imports the `math` module, which provides mathematical functions like `sqrt` (square root), `log` (natural logarithm), and `sin` (sine).

2.  **Error Handling (try-except Block):**
    * `try:`: This block contains the code that might raise exceptions (errors).
        * **User Input:**
            * `num = int(input("enter a number: "))`: Prompts the user to enter a number and converts the input string to an integer.
        * **Mathematical Operations:**
            * `root = math.sqrt(num)`: Calculates the square root of `num`.
            * `print("square root: ", root)`: Prints the calculated square root.
            * `log = math.log(num)`: Calculates the natural logarithm (base e) of `num`.
            * `print("natural logarithm (base e): ", log)`: Prints the calculated natural logarithm.
            * `sine = math.sin(num)`: Calculates the sine of `num` (in radians).
            * `print("sine(radians): ", sine)`: Prints the calculated sine.
    * `except ValueError:`: This block catches `ValueError` exceptions, which occur when the user enters a non-numeric value or a negative number (as `math.sqrt` and `math.log` are not defined for negative numbers).
        * `print("Invalid input. Please enter a non-negative number.")`: Prints an error message informing the user about the invalid input.
    * `except Exception as e:`: This block catches any other exceptions that might occur (e.g., `TypeError`, `ZeroDivisionError`, etc.).
        * `print(f"An error occurred: {e}")`: Prints a generic error message along with the specific error details.

