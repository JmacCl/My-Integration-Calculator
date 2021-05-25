

def oneVariable():

    userInputTwo = input("Integrate what number")
    inputList = []

    for cha in userInputTwo:
        inputList.append(cha)

    print(inputList)

    numberString = ""
    readBool = False
    multiplier = ""

    for numbers in inputList:

        if (numbers != "x" ):
            numberString+= numbers
        else:
            break

    print(numberString)

    for cha in inputList:

        if (cha == '^'):
            readBool = True
        elif (readBool):
            multiplier+= cha

    print(multiplier)

    multiplier = int(multiplier) + 1

    newFront = int(numberString) // multiplier

    print(str(newFront)+'x^' + str(multiplier))





