# QUIZ GAME
print ("Welcome to the quiz game!")

playing = input("Would you like to play? ")
# 
if playing.lower() != "yes":
    quit()
print("Okay! let's play")


score = 0
answer = input("What is CPU in full? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is RAM in full? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is PU in full? ")
if answer.lower() == "power unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What is LCD in full? ")
if answer.lower() == "liquid crystal display":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

    print("You got"  +   str(score)   +  "questions correct")
    