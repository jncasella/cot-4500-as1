import numpy as np
import math

# Converts binary double to decimal double
def binToDouble(binNum):
    m: float = 0

    c = int(binNum[1:12], 2)

    for i in range(12, len(binNum)):
        m += int(binNum[i]) * (1 / 2) ** (i - 11)
    return (-1) ** int(binary[0]) * 2 ** (c - 1023) * (1 + m)

# Gets the number of digits before the decimal of the float passed
def getWholeDigits(num):
    digits = 0
    while (num != 0):
        num //= 10
        digits += 1
    return digits

# Chops the float passed to n digits
def chop(num, n):
    digits = getWholeDigits(num)
    
    num = num / 10 ** digits
    num = math.floor(num * 10 ** n)
    
    return num * 10 ** (digits - n)

# Round the float passed to n digits (whole or decimal)
def newRound(num, n):
    digits = getWholeDigits(num)
    
    num = num / 10 ** digits
    num += 5 * 10 ** (-n - 1)
    
    return chop(num * 10 ** digits, n)

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

# Uses the bisection method to find a zero of the NumPy function object passed to it
#       between left and right with specified precision. Returns iterations needed
def bisectionMethod(f, left, right, precision):
    precision = 10 ** precision
    iterations = 0
    
    while(abs(left - right) > precision):
        iterations += 1
        p = (left + right) / 2
        
        if ((f(left) > 0 and f(p) < 0) or (f(left) < 0 and f(p) > 0)):
            right = p
        else:
            left = p
    
    return iterations

# Uses the Newton-Raphson method to find the nearest root of the NumPy function
#       object passed to it of the approximated value, within
#       a specified precision within a maximum number of iterations
def newtonRaphson(f, aprox, precision, maxIts):
    precision = 10 ** precision
    iterations = 1
    derivative = f.deriv()
    
    while(iterations <= maxIts):
        if (f(aprox) != 0):
            aproxNext = aprox - f(aprox) / derivative(aprox)
        
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
print(chop(num, 3), end = '\n\n')
# End of question 2


# Question 3
roundNum = newRound(num, 3)
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
func = np.poly1d([1, 4, 0, -10])
a = -4
b = 7
bisect = bisectionMethod(func, a, b, -4)
print(bisect)
print(newtonRaphson(func, b, -4, bisect))
# End of question 6