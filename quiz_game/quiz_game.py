print("Welcome to the Quiz Game!!!")

play = input("Do you want to play? ")

if play.lower() == "yes":
    print(" \nOkay! Let´s play :)")
else:
    print("Good bye! :(")
    quit()

score = 0

""" QUESTIONS """

print("\nQuestion number one:")
answerOne = input("Which is the planet closest to the sun? \n\n - Mercury \n - Venus \n - Saturn \n - Earth \n\n answer: ")

if answerOne.lower() == "mercury":
    print("\nCorrect!")
    score += 1
else:
    print("\nIncorrect!")

print("\nQuestion number two:")
answerTwo = input("Which is the smallest country in the world \n\n - Malta \n - Maldivas \n - Monaco \n - Vatican \n\n answer: ")

if answerTwo.lower() == "vatican":
    print("\nCorrect!")
    score += 1
else:
    print("\nIncorrect!")

print("\nQuestion number three:")
answerThree = input("What restaurant has a clown as a pet? \n\n - Mcdonalds \n - Burger King \n - KFC \n - Wendys \n\n answer: ")

if answerThree.lower() == "mcdonalds":
    print("\nCorrect!")
    score += 1
else:
    print("\nIncorrect!")

print("\nQuestion number four:")
answerFour = input("How many horns did a triceratops have? \n\n - Four \n - Two \n - Five \n - Three \n\n answer: ")

if answerFour.lower() == "three":
    print("\nCorrect!")
    score += 1
else:
    print("\nIncorrect!")

print("\nQuestion number five:")
answerFive = input("What cartoon lives in a pineapple under the sea? \n\n - Nemo \n - Flounder \n - Simba \n - Spongebob \n\n answer: ")

if answerFive.lower() == "spongebob":
    print("\nCorrect!")
    score += 1
else:
    print("\nIncorrect!")

print("\nQuestion number six:")
answerSix = input("Which country produces the most coffee in the world? \n\n - Colombia \n - Indonesia \n - Brazil \n - Vietnam \n\n answer: ")

if answerSix.lower() == "brazil":
    print("\nCorrect!")
    score += 1
else:
    print("\nIncorrect!")

print("\nQuestion number seven:")
answerSeven = input("What was the first soda drink that was taken into space? \n\n - Pepsi \n - Fanta \n - Coca Cola \n - Dr Pepper \n\n answer: ")

if answerSeven.lower() == "coca cola":
    print("\nCorrect!")
    score += 1
else:
    print("\nIncorrect!")

print("\nQuestion number eight:")
answerEight = input("What email service is owned by Microsoft? \n\n - Outlook \n - Gmail \n - Icloud mail \n - Yahoo mail \n\n answer: ")

if answerEight.lower() == "outlook":
    print("\nCorrect!")
    score += 1
else:
    print("\nIncorrect!")

print("\nQuestion number nine:")
answerNine = input("What is Chandler's middle name in Friends? \n\n - Arthur \n - Bing \n - Muriel \n - John \n\n answer: ")

if answerNine.lower() == "muriel":
    print("\nCorrect!")
    score += 1
else:
    print("\nIncorrect!")

print("\nQuestion number ten:")
answerTen = input("In the Matrix, what is the color of the pill that Neo takes? \n\n - Red \n - Blue \n - Yellow \n - Orange \n\n answer: ")

if answerTen.lower() == "red":
    print("\nCorrect!\n")
    score += 1
else:
    print("\nIncorrect!\n")


if score == 10:
    print("Perfect Score!!!, your score is " + str(score) + "/10")
elif score > 5 and score < 10:
    print("You Win!!!, your score is " + str(score) + "/10")
else:
    print("You lose!!!, your score is " + str(score) + "/10")