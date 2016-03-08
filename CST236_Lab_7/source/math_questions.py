from math import factorial
from decimal import Decimal, getcontext
import time
from datetime import datetime
import random

def fibonacci(a=0):

    if not (isinstance(a, (int, float))):
        return "invalid"
    if a < 0:
        return "invalid"

    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)

    return fib(a)

def pi(a=0):

    if not (isinstance(a, (int, float))):
        return "invalid"
    if a < 0:
        return "invalid"

    def calc(b=0):
        getcontext().prec=int(b)
        return sum(1/Decimal(16)**k *
          (Decimal(4)/(8*k+1) -
           Decimal(2)/(8*k+4) -
           Decimal(1)/(8*k+5) -
           Decimal(1)/(8*k+6)) for k in range(100))


    s = str(calc(a))[int(a-1)]
    return int(s)




def toFractions(a=''):
        if a == 'nm':
            return 0.000001
        if a == 'cm':
            return 10.0
        if a == 'm':
            return 1000.0
        if a == 'mm':
            return 1.0
        if a == 'km':
            return 1000000.0
        if a == 'in':
            return 25.4
        if a == 'ft':
            return 304.8
        if a == 'yd':
            return 914.4
        if a == 'mi':
            return 1609344.0


def unitConvert(number=0.0, unit1='', unit2=''):

    temp = number * toFractions(unit1) / toFractions(unit2)

    return float("%.2f" % temp)


def conversionVariations():
    return 'nm, mm, cm, m, km, in, ft, yd, mi'

    #toFractions()

def romanNumeralConversion(roman):

        roman_hash = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        for numerals in roman:
            if numerals in roman_hash:
                num += roman_hash[numerals]
            else:
                return "Invalid input"

        if 'IV' in roman :
            num -= 2
        if 'IX' in roman :
            num -= 2
        if 'XL' in roman :
            num -= 20
        if 'XC' in roman :
            num -= 20
        if 'CD' in roman :
            num -= 200
        if 'CM' in roman :
            num -= 200

        return num

def checkLegalAge(dob):

    born = datetime.strptime(dob , '%Y-%m-%d')
    today = datetime.now()

    if born > today:
        return "Invalid"
    else:
        age = today.year - born.year

        if age < 16:
            return "Not legal to drive"

        return "Legal to drive"

def randomNumberRange(a=0, b=0):
    if a == b:
        return "Invalid range"
    randNum = random.randrange(a, b, 1)
    return randNum
