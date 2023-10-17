import json

fin = open("dictionary.json", "r")

cont = json.load(fin)

def dispwords():
    letter = input("Enter the letter to display words with which it begins with: ")
    for i in cont:
        if i.startswith(letter):
            print(i)

def findword():
    word = input("Enter the word to check in the dicionary: ").lower()
    found = False
    for i in cont:
        if i == word:
            found =True
    if found == False:
        print("No such word in the dictionary!")
    else:
        print("It is there in the dictionary.")

def dispmeaning():
    word = input("Enter word to check meaning: ").lower()
    found = False
    for key,value in cont.items():
        if key == word:
            found = True
            print("{} word has meaning {}".format(key,value))
    if found == False:
        print("No such word exists.")

def dispspecmean():
    word = input("Enter word to be searched and display it's meaning: ").lower()
    found = False
    for key,value in cont.items():
        if key == word or word in value:
            found = True
            print("word {} -meaning {}".format(key,value))
    if found == False:
        print("No such word in dictionary.")

def searchno():
    num = int(input("Enter number of letters of the length of the word: "))
    found = False
    for key in cont:
        if len(key) == num:
            print(key)
            found = True
    if found == False:
        print("No words with this specific length!")



while True:
    try:
        print("""
              I N T E R A C T I V E  D I C T I O N A R Y
              ===========================================
              1. Display the word that begins with a specific letter
              2. Find a specific word
              3. Display the meaning of the specific word
              4. Display the word's meaning for the specific word 
              that is there in the meaning
              5. Search and display words by the number of letters
              6. Exit
              """)
        choice = int(input("Enter choice of operation(1-6): "))
        if choice == 1:
            dispwords()
        elif choice == 2:
            findword()
        elif choice == 3:
            dispmeaning()
        elif choice == 4:
            dispspecmean()
        elif choice == 5:
            searchno()
        elif choice == 6:
            break
        else:
            print("Invalid input! Enter number between 1 and 6.")
    except:
        print("Invalid input")