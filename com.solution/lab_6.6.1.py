# Type your code here
keepGoing = True
doesntHaveComma = False
while keepGoing:
    userInput = ''
    userInput = input("Enter input string: \n")

    if "q" in userInput.replace(" ", ""):
        keepGoing = False
        continue
    elif "," not in userInput:
        print("Error: No comma in string.")
        doesntHaveComma = True
    else:
        names = userInput.replace(" ", "").split(",")
        print('First word: ' + names[0])
        print('Second word: ' + names[1])

    if doesntHaveComma == False:
        print('\n')