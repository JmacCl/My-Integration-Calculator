'''
This is the process of hw this integration calculator works:

1. Take in input from user, determine if you want to integrate between 2 points or not.
2. Call a function to Separate the expressions from the operations in the input.
and put each of the distinct items in a list, which in turn is returned.
3. Call a function that returns a list of commands for each expression from the above created list
4. Call a integration function that looks through each of the expression and commands and
allocates each expression with their associative commands.
5. Once each expression has been integrated, return the fully integrated input.
'''

operationList = ['+','-']
ignoreList = ['',' ']
trigList = {'sin','cos','tan','csc','sec','cot'}
hyperbolicTrigList = ['sinh','cosh','tanh','csch','sech','coth']
otherList = ['e','ln']
ignoreWhenFirstScanning = ['x','^']
simpleTrigPlusHyperbolicDict = {'sin':'-cos','cos':'sin',
                                'cosh':'sinh', 'sinh':'cosh'}
doesWantToIntegrateBetweenPoints = False


# Maybe in divide, make a sepaerate list that contans messages of integrate each variable, wether it be
# exponential, basic, by parts, etc...



#Divide and check both splits the input into expression and operations, while also
# assigning each expression a command for how it will be integrated
def receiveInput():
    expressionInput  = input("What is the expression you would like to integrate?: ")
    betweenNumbersCheck = input('Would you like to integrate between two points?: ')
    if betweenNumbersCheck == 'yes':
        doesWantToIntegrateBetweenPoints = True
        inputPoints = input('What are the 2 points (Please separate each by a comma): ')
        return [expressionInput,inputPoints]
    else:
        return [expressionInput,'']


def divide():
    #Check what number to integrate
    userInputTwo = input("Integrate what number: ")
    compositeList = []
    inputString = ''
    # list of booleanOperations:
    #Break input into seperate parts
    readOperations = False
    for cha in userInputTwo:
        if cha == '(':
            readOperations = True
            inputString += cha
        elif cha == ')':
            readOperations = False
            inputString += cha
        elif(readOperations):
            inputString += cha
        elif (cha != '') and cha not in operationList:
            inputString += cha
        else:
            compositeList.append(inputString)
            compositeList.append(cha)
            inputString = ''
    compositeList.append(inputString)
    return compositeList

def classifyIntegrals(inputList):
    readOperations = False
    commandList = []
    finishedLooking = False
    exponentialTrigger = False
    integral = ''
    trigHolder = ''
    readTrig = False
    for expressions in inputList:
        if expressions in operationList:
            commandList.append('ignore')
        else:
            for cha in expressions:
                if cha == 'e':
                    commandList.append('exponential')
                    finishedLooking = True
                    break
                elif cha == 'c':
                    commandList.append('trig')
                    finishedLooking = True
                    break
                elif cha == 't':
                    commandList.append('trig')
                    finishedLooking = True
                    break
                elif cha == 's':
                    commandList.append('trig')
                    finishedLooking = True
                    break
                elif cha == '(':
                    readOperations = True
                elif cha == ')':
                    readOperations = False
                elif (cha == '-' and readOperations):
                    exponentialTrigger = True
                elif exponentialTrigger and cha == '1':
                    commandList.append('naturalLog')
                    finishedLooking = True
                    break
            if not finishedLooking:
                commandList.append('simple')
    return commandList


def allocateIntegration(expressionList,commandList):
    countOfIntegrals: int = 0
    while countOfIntegrals < len(expressionList):
        if commandList[countOfIntegrals] == 'exponential':
            expressionList[countOfIntegrals] = exponentialIntegration(expressionList[countOfIntegrals])
        elif commandList[countOfIntegrals] == 'naturalLog':
            expressionList[countOfIntegrals] = integrationByNaturalLog(expressionList[countOfIntegrals])
        elif commandList[countOfIntegrals] == 'simple':
            expressionList[countOfIntegrals] = integrateSimple(expressionList[countOfIntegrals])
        elif commandList[countOfIntegrals] == 'trig':
            expressionList[countOfIntegrals] = integrateTrig(expressionList[countOfIntegrals])
        countOfIntegrals += 1


def integrateSimple(inputExpression):
        recordIfNegative = False

        ''' 
        numberString includes the constant coefficient next to variable,
        readBool is used so that certain parts of the expression can be read,
        multiplier is the string number that'll be brought own to be integrated
        '''
        noPower = True
        numberString = ""
        readBool = False
        multiplier = ""
        '''The below for loop reads the coefficent at the front '''
        for numbers in inputExpression:
            if (numbers != "x" ):
                numberString += numbers
            else:
                noPower = False
                break
        if noPower:
            return numberString + 'x'
        '''This scan reads the power'''
        for cha in inputExpression:
            if (cha == '^'):
                readBool = True
            elif (readBool):
                if cha != '(' and cha != ')' :
                    multiplier += cha
                if cha == '-':
                    recordIfNegative = True

        '''The below code add a number to the power, 
        divides the coefficient by the new power, then reconstructs the new
        expression and adds it back to the list'''
        multiplier = float(multiplier) + 1
        newFront = float(numberString) / multiplier
        if recordIfNegative:
            inputExpression = str(newFront)+'x^(' + str(multiplier) + ')'
        else:
            inputExpression = str(newFront)+'x^' + str(multiplier)
        return inputExpression


def integrateByParts():
    pass

def exponentialIntegration(inputExpression):
    recordIfNegative = False
    numberString = ""
    readBool = False
    multiplier = ""
    '''The below for loop reads the coefficent at the front '''
    for numbers in inputExpression:
        if (numbers != "e" ):
            numberString += numbers
        else:
            break
    if numberString == '':
        numberString = '1'
    '''This scan reads the power'''
    for cha in inputExpression:
        if (cha == '^'):
            readBool = True
        elif (readBool):
            if cha == 'x':
                break
            if cha != '(' and cha != ')' :
                multiplier += cha
            if cha == '-':
                recordIfNegative = True

    '''The below code add a number to the power, 
    divides the coefficient by the new power, then reconstructs the new
    expression and adds it back to the list'''
    multiplier = int(multiplier)
    newFront = int(numberString) / multiplier

    inputExpression = str(newFront)+'e^(' + str(multiplier) + 'x)'

    return inputExpression

def integrationByVariable():
    pass

def integrateTrig(inputExpression):
    frontString = ''
    trigString =''
    endString = ''
    bracketString = ''
    readBracket = False
    readFront = True
    for numbers in inputExpression:
        if numbers.isdigit() and readFront:
            frontString += numbers
        else:
            endString += numbers
            readFront = False
    for cha in endString:
        if cha == 'x':
            break
        elif cha != '(' and not readBracket:
            trigString += cha
        elif readBracket:
            bracketString += cha
        else:
            readBracket = True
    newFront = ''
    if bracketString == '':
        bracketString = 1
    if frontString == '':
        frontString = 1
    newFront = str(int(frontString)/int(bracketString))
    if newFront == '1.0':
        newFront = ''
    if bracketString == 1:
        bracketString = ''
    if trigString == 'cos':
        return newFront + 'sin('+str(bracketString)+ 'x)'
    elif trigString == 'sin':
        return '-' + newFront + 'cos('+str(bracketString)+ 'x)'

def integrationByNaturalLog(inputExpression):
    numberString = ""
    variableString = ''
    readExpressionBracket = False
    readExpression = True
    '''The below for loop reads the coefficent at the front '''
    for numbers in inputExpression:
        if (numbers != "x" and numbers != '(' ):
            numberString += numbers
        else:
            break
    for numbers in inputExpression:
        if numbers == '(':
            readExpressionBracket = True
        elif numbers == ')':
            readExpressionBracket = False
            break
        elif (readExpressionBracket):
            variableString += numbers
    return numberString + 'ln(' + variableString+')'

def rebuild(inputList):

     returnString = ''
     for expressions in inputList:
         returnString += expressions + ' '
     return returnString


def oneVariable():

    processedInputList = divide()
    commandList = classifyIntegrals(processedInputList)
    allocateIntegration(processedInputList,commandList)

    return rebuild(processedInputList)



##This is the second version of integration
# def divide():
#     #Check what number to integrate
#     userInputTwo = input("Integrate what number: ")
#     compositeList = []
#     commandList = []
#     inputString = ''
#     # list of booleanOperations:
#     foundExponential = False
#     #Break input into seperate parts
#     readOperations = False
#     for cha in userInputTwo:
#         if cha == '(':
#             readOperations = True
#             inputString += cha
#         elif cha == ')':
#             readOperations = False
#             inputString += cha
#         elif(readOperations):
#             inputString += cha
#         elif (cha != '') and cha not in operationList:
#             inputString += cha
#         else:
#             compositeList.append(inputString)
#             compositeList.append(cha)
#             inputString = ''
#     compositeList.append(inputString)
#     print(compositeList)
#     return compositeList
# def integrate(inputList):
#     # For keeping record on index of list that includes all terms of the
#     #integral
#     indexRecord = 0
#     recordIfNegative = False
#     '''Loops through the entire inputList, which
# is the broken down input of the expression made in divide'''
#     for expressions in inputList:
#         #If the expression is not a operation
#         if expressions not in operationList:
#             '''
# numberString includes the constant coefficient next to variable,
# readBool is used so that certain parts of the expression can be read,
# multiplier is the string number that'll be brought own to be integrated
# '''
# numberString = ""
# readBool = False
# multiplier = ""
# '''The below for loop reads the coefficent at the front '''
#             for numbers in expressions:
#                 if (numbers != "x" ):
#                     numberString += numbers
#                 else:
#                     break
#             '''This scan reads the power'''
#             for cha in expressions:
#                 if (cha == '^'):
#                     readBool = True
#                 elif (readBool):
#                     if cha != '(' and cha != ')' :
#                         multiplier += cha
#                     if cha == '-':
#                         recordIfNegative = True
#             print(multiplier)
#
#             '''The below code add a number to the power,
# divides the coefficient by the new power, then reconstructs the new
# expression and adds it back to the list'''
#
#             if multiplier == '-1':
#                 inputList[indexRecord] = numberString + 'ln(x)'
#                 indexRecord += 1
#             else:
#                 multiplier = int(multiplier) + 1
#                 newFront = int(numberString) / multiplier
#                 if recordIfNegative:
#                     inputList[indexRecord] = str(newFront)+'x^(' + str(multiplier) + ')'
#                 else:
#                     inputList[indexRecord] = str(newFront)+'x^' + str(multiplier)
#                 indexRecord += 1
#         else:
#             indexRecord += 1
#     return inputList
#
# def rebuild(inputList):
#
#      returnString = ''
#      for expressions in inputList:
#          returnString += expressions + ' '
#      return returnString
#
#
# def oneVariable():
#
#     processedInput = divide()
#     processedIntegral = integrate(processedInput)
#     return rebuild(processedIntegral)






# def oldOneVariable():
#
#     #Check what number to integrate
#     userInputTwo = input("Integrate what number")
#     inputList = []
#
#     #Break input into seperate parts
#     for cha in userInputTwo:
#         if cha != '':
#             inputList.append(cha)
#
#     numberString = ""
#     readBool = False
#     multiplier = ""
#
#     #30x^5 +
#
#     for numbers in inputList:
#         if (numbers != "x" ):
#             numberString += numbers
#         else:
#             break
#
#     for cha in inputList:
#         if (cha == '^'):
#             readBool = True
#         elif (readBool):
#             multiplier += cha
#
#
#     multiplier = int(multiplier) + 1
#
#     newFront = int(numberString) / multiplier
#
#     return (str(newFront)+'x^' + str(multiplier))



