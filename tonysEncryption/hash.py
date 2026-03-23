from encrypt import *
import math

def rasePower(ascciArr, exponent):
    convertedValues = []
    for val in ascciArr:
        convertedValues.append(math.pow(val, exponent))

    return convertedValues

def modulus(arr, val):
    convertedValues = []
    for num in arr:
        convertedValues.append(num % val)

    return convertedValues

def hash(word):
    convertedWord = toAscii(word)
    convertedWord = rasePower(convertedWord, 999)
    convertedWord = modulus(convertedWord, 364)
    return convertedWord
