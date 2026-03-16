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




def encryptWithTable(word, key):
    table = makeTable(superSecretWord)
    














#AI made this
def printTable(table):
    print("\n--- Generated Cipher Square ---")
    
    # Loop through the table, keeping track of the row number (i) and the row data
    for i, row in enumerate(table):
        # Format the row number to always be at least two digits (e.g., 00, 01, 10)
        # to keep everything perfectly aligned
        print(f"Row {i:02d}: {row}")
        
    print("-------------------------------\n")


foo = makeTable("kryptos KRYPTOS")
printTable(foo)
