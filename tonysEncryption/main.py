from decrypt import encryptString, decryptString
from vigenereTable import encryptWithTable, decryptWithTable

def main():
    inputWord = " like to eat my ham. It makes me feel like shlam. Have you seen the movie Kazam? But back to ham. Did you know that an imam is a man who leads the prayer in a mosque? What if you pronounced imam, e-mam? Would that make you think of ham? My name is Stan. Ham."

    # encrypting with base 64 and random nonsense first assingment
    randomVal = 98154164 
    encryptedWord = encryptString(inputWord, randomVal)
    decryptedWord = decryptString(encryptedWord, randomVal)

    print("------ENCRYPTING WITH BASE 64------")
    print()
    print("encrypted string: " + encryptedWord)
    print("decrypted string: " + decryptedWord)



    # encrypting with vigenere table second assingment
    superSecretKey = "[:KV&jHc3fHkQBC"
    encryptedWord = encryptWithTable(inputWord, superSecretKey)
    decryptedWord = decryptWithTable(encryptedWord, superSecretKey)

    print()
    print("------ENCRYPTING WITH VIGENERE TABLE------")
    print()
    print("encrypted string: " + encryptedWord)
    print("decrypted string: " + decryptedWord)


main()


