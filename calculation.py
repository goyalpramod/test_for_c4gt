import math

def add(x: float, y: float) -> float:
    """
    Add two numbers.

    Parameters:
    - x (float): The first operand.
    - y (float): The second operand.

    Returns:
    float: The sum of x and y.
    """
    return x + y

def subtract(x: float, y: float) -> float:
    """
    Subtract y from x.

    Parameters:
    - x (float): The minuend.
    - y (float): The subtrahend.

    Returns:
    float: The result of subtracting y from x.
    """
    return x - y

def multiply(x: float, y: float) -> float:
    """
    Multiply two numbers.

    Parameters:
    - x (float): The first factor.
    - y (float): The second factor.

    Returns:
    float: The product of x and y.
    """
    return x * y

def divide(x: float, y: float) -> float:
    """
    Divide x by y.

    Parameters:
    - x (float): The numerator.
    - y (float): The denominator.

    Returns:
    float: The result of dividing x by y.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def power(x: float, y: float) -> float:
    """
    Raise x to the power of y.

    Parameters:
    - x (float): The base.
    - y (float): The exponent.

    Returns:
    float: x raised to the power of y.
    """
    return x ** y

def square_root(x: float) -> float:
    """
    Calculate the square root of x.

    Parameters:
    - x (float): The number for which to find the square root.

    Returns:
    float: The square root of x.
    """
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(x)

def factorial(x: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    Parameters:
    - x (int): The non-negative integer for which to calculate the factorial.

    Returns:
    int: The factorial of x.
    """
    if x < 0:
        raise ValueError("Factorial is undefined for negative numbers")
    return math.factorial(x)

def logarithm(x: float, base: float = 10) -> float:
    """
    Calculate the logarithm of x with a specified base.

    Parameters:
    - x (float): The number for which to calculate the logarithm.
    - base (float, optional): The base of the logarithm (default is 10).

    Returns:
    float: The logarithm of x with the specified base.
    """
    if x <= 0 or base <= 0 or base == 1:
        raise ValueError("Invalid input for logarithm calculation")
    return math.log(x, base)