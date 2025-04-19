def fact(num):
    """Calculate factorial of a number"""
    factorial = 1
    for i in range(num, 0, -1):
        factorial *= i
    return factorial 