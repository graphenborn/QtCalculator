from math import *

def decdeg2dms(dd, num2):
    mult = -1 if dd < 0 else 1
    mnt,sec = divmod(abs(dd)*3600, 60)
    deg,mnt = divmod(mnt, 60)
    return mult*deg, mult*mnt, mult*sec

operationsDict = {
			"+" : (lambda num1, num2: num1 + num2),
            "-" : (lambda num1, num2: num1 - num2),
            "/" : (lambda num1, num2: num1 / num2),
            "*" : (lambda num1, num2: num1 * num2),
            "√" : (lambda num1, num2=0: sqrt(num1)),
            "^" : (lambda num1, num2: num1 ** num2),
            "Dms" : decdeg2dms,
            "10^" : (lambda num1, num2=0: 10**num1),
            "tanh" : (lambda num1, num2: tanh(num1)),
            "Ln" : (lambda num1, num2: log(num1))
		}

def calculate(num1, operation, num2):
    if num1 == "Pi":
        num1 = pi
    elif num2 == "Pi":
        num2 = pi
    for i in operationsDict:
        if i == operation:
            result = operationsDict[i](float(num1), float(num2))
            return result