import random


superSecretWord = "kryptos KRYPTOS"


#the key cant have any duplicate chars
def makeTable(ShiftingWord):

    charters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '

    for char in ShiftingWord:
        charters = charters.replace(char, "")


    startingRow = ShiftingWord + charters
    
    table = [startingRow]

    for i in range(len(startingRow) - 1):
        temp = table[i][0]
        newRow = table[i][1:] + temp
        table.append(newRow)

    return table



def encryptWithTable(string, key):

    while(len(string) > len(key)):
        key += key
        if(len(string) < len(key)):
            key = key[0:len(string)]

       
    table = makeTable(superSecretWord)
    #printTable(table)
    newString = ""

    for i in range(0, len(string)):

        col = table[0].index(string[i])

        for j in range(0, len(table)):

            row = 0
            if(table[j][0] == key[i]):
                row = j
                break

        newString += table[row][col]
    
    return newString

    

def decryptWithTable(string, key):

    while(len(string) > len(key)):
        key += key
        if(len(string) < len(key)):
            key = key[0:len(string)]

       
    table = makeTable(superSecretWord)
    convertedString = ""

    for i in range(len(string)):

        row = 0
        for j in range(len(table)):
            if table[j][0] == key[i]:
                row = j
                break
        

        col = table[row].index(string[i])
        convertedString += table[0][col]


    return convertedString


def generateKey(length):
    charters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
    
    key = ""
    
    for i in range(length):
        randIndex = random.randint(0, len(charters) - 1)
        key += charters[randIndex]
    
    return key



#AI made this
def printTable(table):
    print("\n--- Generated Cipher Square ---")
    
    # Loop through the table, keeping track of the row number (i) and the row data
    for i, row in enumerate(table):
        # Format the row number to always be at least two digits (e.g., 00, 01, 10)
        # to keep everything perfectly aligned
        print(f"Row {i:02d}: {row}")
        
    print("-------------------------------\n")



#to make an uniqe key every time i run this file becuse im lazy
print(generateKey(15))