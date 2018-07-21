import math


def factorial(n):
    if n == "Error":
        return "Error"
    elif n == "":
        return "Error"
    else:
        n = float(n)
        n = int(n)
        ans = n

        if n == 0:
            return 1

        elif n < 0:
            return "Syntax Error"

        while n > 1:
            if n > 40:
                return "Value too big"
            else:
                ans = ans * (n - 1)
                n -= 1
        return ans


def to_roman(n):
    try:
        n = int(n)
    except:
        return "Syntax Error"

    if n > 4999:
        return "Number out of range"

    num_breaks = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    letters = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    result = ""
    for value in num_breaks:
        while n >= value:
            result += letters[value]
            n = n - value
    return result


def to_binary(n):
    try:
        n = int(n)
        return bin(n)[2:]
    except:
        return "Syntax Error"


def from_binary(n):
    try:
        return int(n, 2)
    except:
        return "Syntax Error"


def sqrt(n):
    if n == "Error":
        return "Error"
    elif n == "":
        return "Error"
    elif float(n) < 0:
        return "Error"
    else:
        n = float(n)
        ans = n ** 0.5
    return ans


def cube_root(n):
    if n == "Error":
        return "Error"
    elif n == "":
        return "Error"
    elif float(n) < 0:
        return "Error"
    else:
        n = float(n)
        ans = n ** (1/3)
    return ans


def raised_to_2(n):
    if n == "-----> Result too Large":
        return "Error"
    elif n == "Error":
        return "Error"
    elif n == "":
        return "Error"
    elif float(n) > 2 ** 400:
        return "-----> Result too Large"
    else:
        n = float(n)
        ans = n ** 2
    return ans


def raised_to_3(n):
    if n == "Error":
        return "Error"
    elif n == "":
        return "Error"
    elif float(n) > 2 ** 400:
        return "-----> Result too Large"
    else:
        n = float(n)
        ans = n ** 3
    return ans


def natural_log(n):
    if n == "Error":
        return "Error"
    elif n == "":
        return "Error"
    elif float(n) == 0:
        return "Error"
    elif float(n) < 0:
        return "Error"
    else:
        n = float(n)
        ans = math.log(n)
    return ans


def logarithm(n):
    if n == "Error":
        return "Error"
    elif n == "":
        return "Error"
    elif float(n) == 0:
        return "Error"
    elif float(n) < 0:
        return "Error"
    else:
        n = float(n)
        ans = math.log10(n)
    return ans


def sine(n):
    if n == "Error":
        return "Error"
    else:
        n = float(n)
        ans = math.sin(n)
        return ans


def cosine(n):
    if n == "Error":
        return "Error"
    else:
        n = float(n)
        ans = math.cos(n)
        return ans


def tangent(n):
    if n == "Error":
        return "Error"
    else:
        n = float(n)
        ans = math.cos(n)
        return ans


def delete(n):
    n2 = n.split()
    print(n2)
    del n2[-1]
    print(n2)
    temp = ""
    for i in n2:
        temp = temp + i + " "
        print(temp)
    return temp

