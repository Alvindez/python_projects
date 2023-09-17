# QUIZ GAME
print ("Welcome to the quiz game!")

playing = input("Would you like to play? ")
# 
if playing.lower() != "yes":
    quit()
print("Okay! let's play")

answer = input("What is CPU in full? ")
if answer.lower() == "Central Processing Unit":
    print("Correct!")
else:
    print("Incorrect")

answer = input("What is RAM in full? ")
if answer.lower() == "Random Access Memory":
    print("Correct!")
else:
    print("Incorrect")

answer = input("What is PU in full? ")
if answer.lower() == "Power Unit":
    print("Correct!")
else:
    print("Incorrect")

answer = input("What is LCD in full? ")
if answer.lower() == "Liquid Crystal Display":
    print("Correct!")
else:
    print("Incorrect")