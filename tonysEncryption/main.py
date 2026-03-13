import math


def toAscii(baseString):
    convertedValues = []
    for char in baseString:
        convertedValues.append(ord(char))
    return convertedValues

def addRandomVal(asciiArr, val):
    convertedValues = []
    for num in asciiArr:
        convertedValues.append(num + val)
    return convertedValues


def bitShift(asciiArr, shiftAmt):
    convertedValues = []
    for val in asciiArr:
        convertedValues.append(math.ceil(val / (shiftAmt *  2)))
    return convertedValues

def toBinary(asciiArr):
    convertedValues = []
    for val in asciiArr:
        convertedValues.append(format(val, '08b'))
    return convertedValues


def toBase64(vals):
    vals = toBinary(vals)
    b64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    binaryString = ""
    for binary in vals:
        binaryString += binary
    
    groupedVals = []
    for i in range(0, len(binaryString), 6):
        groupedVals.append(binaryString[i:i+6])
        
    base64String = ""
    for group in groupedVals:
        decimal_val = int(group, 2)
        base64String += b64_chars[decimal_val]
        
    return base64String

    

def encrypt(word):
    randomVal = 32
    asciiVals = toAscii(word)
    pulseRandomVal = addRandomVal(asciiVals, randomVal)
    shiftedBinary = (bitShift(pulseRandomVal, 1)) 
    base64 = toBase64(shiftedBinary)


    # print("starting string: " + word)
    # print("ascii:   " + str(toBinary(asciiVals)))
    # print("added:   " + str(toBinary(pulseRandomVal)))
    # print("shifted: " + str(toBinary(shiftedBinary)))
    # print("base 64: " + str(base64))
    return base64


def main():
    inputWord = "Hello World!"
    encryptedWord = encrypt(inputWord)
    print("starting string:  " + inputWord)
    print("encrypted string: " + encryptedWord)


main()






def checkForDuplicatesInWordList():
    dictionaryOfWords = {}
    with open("bigListOfWords.txt") as myFile:
        for eachWord in myFile:
            if eachWord in dictionaryOfWords:
                # already in the dictionary?
                dictionaryOfWords[eachWord] += 1
                # print("OOPS " + eachWord + " is already in the dictionaryOfWords", end =" / ")
                # return
            else:
                # add to dictionaryOfHashes and set it to 1 appearance
                dictionaryOfWords[eachWord] = 1
    # print("no duplicates")
    with open("words.txt", "w") as f:
        for key in dictionaryOfWords:
            f.write(key)



# param functionName - the function that will be tested for collisions
# for example, checkForCollisions(rileySuperSecretEncrypt01)
def checkForCollisions(functionName):
    hasCollisions = False
    dictionaryOfHashes = {}
    with open("bigListOfWords.txt") as myFile:
        for eachWord in myFile:
            # get each encrypted version
            encryptedWord = functionName(eachWord.strip("\n"))
            if encryptedWord in dictionaryOfHashes:
                # already in the dictionary?
                dictionaryOfHashes[encryptedWord] += 1
                print("OOPS " + encryptedWord + " is already in the dictionaryOfHashes", end =" / ")
                hasCollisions = True
            else:
                # add to dictionaryOfHashes and set it to 1 appearance
                dictionaryOfHashes[encryptedWord] = 1
    if hasCollisions:
        #print(dictionaryOfHashes)
        print("\nFAIL: we have collisions")
    else:
        print("\nSUCCESS: no collisions")
                


