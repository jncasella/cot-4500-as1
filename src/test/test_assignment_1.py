import math

# Converts binary double to decimal double
def binToDouble(binNum):
    m: float = 0

    c = int(binNum[1:12], 2)

    for i in range(12, len(binNum)):
        m += int(binNum[i]) * (1 / 2) ** (i - 11)
    return (-1) ** int(binary[0]) * 2 ** (c - 1023) * (1 + m)

# Defines the values of a series
def series(x, n):
    return x ** n / n ** 3

# Finds the minimal iterations needed to reach a specific tolerance
def minTerms(precision, val):
    precision = 10 ** precision
    # If evaluation value is one, uses a simple mathematical expression
    #       to find the minimal iterations needed to reach desired precision
    if val == 1:
        return math.ceil(precision ** (-1 / 3))
    
    # If evaluation value is in [0, 1), tracks number of iterations
    #       needed to reach desired precision
    if (val < 1 and val >= 0):
        terms = 1
        while(series(val, terms) > precision):
            terms += 1
        return terms
        
    # If evaluation value is greater than 1 or less than 0, the series
    #       does not converge, thus no value is returned
    else:
        return 'This series does not converge'

# Defines a function to find the roots of with bisection and Newton Raphson methods
def function(x):
    return x ** 3 + 4 * x * x - 10

# Defines the derivative of the function defined in "function()"
def fDer(x):
    return 3 * x * x + 8 * x

# Uses the bisection method to find a zero of the function defined in "function()"
#       between left and right with specified precision. Returns iterations needed
def bisectionMethod(left, right, precision):
    precision = 10 ** precision
    iterations = 0
    
    while(abs(left - right) > precision and iterations < 1000):
        iterations += 1
        p = (left + right) / 2
        
        if ((function(left) > 0 and function(p) < 0)\
         or (function(left) < 0 and function(p) > 0)):
            right = p
        else:
            left = p
    
    return iterations

def newtonRaphson(aprox, precision, maxIts):
    precision = 10 ** precision
    iterations = 1
    
    while(iterations <= maxIts):
        if (fDer(aprox) != 0):
            aproxNext = aprox - function(aprox) / fDer(aprox)
        
            if (abs(aprox - aproxNext) < precision):
                return iterations
            
            iterations += 1
            aprox = aproxNext
        
        else:
            return 'Derivative is zero'
    return 'Max iterations reached'
    

# Question 1
binary = "010000000111111010111001"

num = binToDouble(binary)

print("%.5f" % num, end="\n\n")
# End of question 1


# Question 2
temp = num
digits = 0

while temp != 0:
    temp //= 10
    digits += 1
chopNum = num / 10 ** digits

# Chop to 3 digits
chopNum = math.floor(chopNum * 10 ** 3)

# Replace decimal point in decNum to appropriate location
chopNum = chopNum * 10 ** digits / 10 ** 3

print("%g" % chopNum, end="\n\n")
# End of question 2


# Question 3
roundNum = num / 10 ** digits

roundNum = round(roundNum, 3)

roundNum = roundNum * 10 ** digits

print("%g" % roundNum, end="\n\n")
# End of question 3

# It is worth noting that for chopping and rounding floats, easier methods exist
#       though this method most closely matches the method discussed in lecture


# Question 4
# Absolute error
print(abs(roundNum - num))

# Relative error
print(abs(roundNum - num) / num, end="\n\n")
# End of question 4


# Question 5
print(minTerms(-4, 1), end = '\n\n')
# End of question 5


# Question 6
a = -4
b = 7
bisect = bisectionMethod(a, b, -4)
print(bisect)
print(newtonRaphson(b, -4, bisect))
# End of question 6