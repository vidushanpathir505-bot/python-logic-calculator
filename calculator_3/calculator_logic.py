import math

# //-----------------\\

def addition(a,b):
    try:
        return f' {a + b:.2f} '
    except ValueError:
        return "Enter valid value"
    
# //-----------------\\

def subtraction(a,b):
    try:
        return f' {a - b:.2f} '
    except ValueError:
        return "Enter valid value"

# //-----------------\\

def multiplication(a,b):
    try:
        return f' {a * b:.2f} '
    except ValueError:
        return "Enter valid value"

# //-----------------\\

def division(a,b):
#Handle division by zero
    if b == 0:
        return "Cannot divide by zero"
    
    return f' {a / b:.2f} '

# //-----------------\\

def power(a,b):
    try:
        return f' {a ** b:.2f} '
    except ValueError:
        return "Enter valid value"

# //-----------------\\

def sqrt(a):
#Handle negative number sqrt
    if a < 0:
        return 'Cannot take square root of negative number'
            
    return f' {math.sqrt(a):.2f} '

# //-----------------\\

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
    "**": power,
    "√": sqrt
}

# //-----------------\\