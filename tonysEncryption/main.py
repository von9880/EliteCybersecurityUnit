from decrypt import encryptString, decryptString

def main():
    inputWord = "Hello World!"
    randomVal = 98154164
    
    encryptedWord = encryptString(inputWord, randomVal)
    decryptedWord = decryptString(encryptedWord, randomVal)
    print()
    print("encrypted string: " + encryptedWord)
    print("decrypted string: " + decryptedWord)


main()


