from decrypt import *
import math

def rasePower(ascciArr, exponent):
    convertedValues = []
    for val in ascciArr:
        convertedValues.append(math.pow(val, exponent))

    return convertedValues

def modulus(arr, val):
    convertedValues = []
    for num in arr:
        convertedValues.append(int(num % val))

    return convertedValues

def hashWord(word):
    convertedWord = toAscii(word)
    convertedWord = rasePower(convertedWord, 99)
    convertedWord = modulus(convertedWord, 127)
    finalWord = ""
    for val in convertedWord:
        finalWord += str(val)
    return finalWord

