import math




def cipher(word, key):
    newWord = ""

    #TODO

    return newWord






def toAscii(baseString):
    convertedValues = []
    for char in baseString:
        convertedValues.append(ord(char))
    return convertedValues

def addRandomVal(asciiArr, val):
    convertedValues = []
    for num in asciiArr:
        convertedValues.append((num + val) % 127)
    return convertedValues


def bitShift(asciiArr, shiftAmt):
    convertedValues = []
    for val in asciiArr:
        convertedValues.append(val << shiftAmt)
    return convertedValues

def toBinary(asciiArr):
    convertedValues = []
    for val in asciiArr:
        convertedValues.append(format(val, '08b'))
    return convertedValues


def toBase64(vals):
    vals = toBinary(vals)
    b64Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    binaryString = ""
    for binary in vals:
        binaryString += binary
    
    groupedVals = []
    for i in range(0, len(binaryString), 6):
        groupedVals.append(binaryString[i:i+6])
        
    last_index = len(groupedVals) - 1
    while len(groupedVals[last_index]) < 6:
        groupedVals[last_index] += "0"

    print(str(groupedVals))
    base64String = ""
    for group in groupedVals:
        foo = 0
        if(group[0] == "1"):
            foo += 32
        if(group[1] == "1"):
            foo += 16 
        if(group[2] == "1"):
            foo += 8
        if(group[3] == "1"):
            foo += 4
        if(group[4] == "1"):
            foo += 2
        if(group[5] == "1"):
            foo += 1
        base64String += b64Chars[foo]
    return base64String



def encrypt(word, randomVal):

    asciiVals = toAscii(word)
    pulseRandomVal = addRandomVal(asciiVals, randomVal)
    shiftedBinary = (bitShift(pulseRandomVal, 1)) 
    base64 = toBase64(shiftedBinary)


    print("starting string: " + word)
    print("ascii:   " + str(asciiVals))
    print("added:   " + str(pulseRandomVal))
    print("shifted: " + str(shiftedBinary))
    print("base 64: " + str(base64))
    return base64


def main():
    inputWord = "hello"
    randomVal = 1324657869764524231
    
    encryptedWord = encrypt(inputWord, randomVal)
    print()
    print("starting string:  " + inputWord)
    print("encrypted string: " + encryptedWord)

main()



