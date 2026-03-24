from encrypt import *



def asciiToChar(asciiArr):
    convertedWord =""
    for val in asciiArr:
        convertedWord += chr(val)
    return convertedWord

def subRandomVal(randomArr, val):
    return addRandomVal(randomArr, (-1 * val))


def base2ToDecmail(binaryArr):
    convertedVals = []
    for binary in binaryArr:
        convertedVals.append(int(binary, 2))
    return convertedVals

def bitShiftRight(asciiArr, shiftAmt):
    convertedValues = []
    for val in asciiArr:
        convertedValues.append(val >> shiftAmt)
    return convertedValues


def base64ToBase2(b64String):
    b64Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    b64Nums = []
    for char in b64String:
        b64Nums.append(b64Chars.index(char))

    ob8Nums = toBinary(b64Nums)

    ob6Nums = []
    for binary in ob8Nums:
        ob6Nums.append(binary[2:8])

    binaryString = ""
    for binary in ob6Nums:
        binaryString += binary

    convertedVals = []
    for i in range(0, len(binaryString) // 8):
        convertedVals.append(binaryString[i * 8:((i+1) * 8)])
    

    return convertedVals


def decryptString(encyptedWord, randomVal):
    invertetedWord = base64ToBase2(encyptedWord)
    ShiftedBinary = invert(invertetedWord)
    shiftedVals = base2ToDecmail(ShiftedBinary)
    randomVals = bitShiftRight(shiftedVals, 1)
    ascii = subRandomVal(randomVals, randomVal)
    decryptedWord = asciiToChar(ascii)
    return(decryptedWord)

   


