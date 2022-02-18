"""
This is the process of how this integration calculator works:

1. Take in input from user, determine if you want to integrate between 2 points or not.
2. Call a function to Separate the expressions from the operations in the input.
and put each of the distinct items in a list, which in turn is returned.
3. Call a function that returns a list of commands for each expression from the above created list
4. Call a integration function that looks through each of the expression and commands and
allocates each expression with their associative commands.
5. Once each expression has been integrated, return the fully integrated input.
"""

"""
Ideas:

- make a class called expressions which represents a mathematical expression
"""


class Expression:
    coefficient: int
    variable: str
    power: str

    def __init__(self, coefficient, variable, power):
        self.coefficient = coefficient
        self.variable = variable
        self.power = power



operationList = ['+', '-']
ignoreList = ['', ' ']
trigList = {'sin', 'cos', 'tan', 'csc', 'sec', 'cot'}
hyperbolicTrigList = ['sinh', 'cosh', 'tanh', 'csch', 'sech', 'coth']
otherList = ['e', 'ln']
ignoreWhenFirstScanning = ['x', '^']
simpleTrigPlusHyperbolicDict = {'sin': '-cos', 'cos': 'sin',
                                'cosh': 'sinh', 'sinh': 'cosh'}
doesWantToIntegrateBetweenPoints = False

"""
NOTES:
- Maybe in divide, make a separate list that contains messages of integrate each variable, whether it be
exponential, basic, by parts, etc...

- Divide and check both splits the input into expression and operations, while also
assigning each expression a command for how it will be integrated

"""


# This code will be used for when implement the integration between two points feature
# def receiveInput():
#     """
#     This function asks the user for the expression that needs to be integrated and if the user would like to
#     integrate the expression between two given points. It returns the given expression
#     :return:
#     """
#     expressionInput = input("What is the expression you would like to integrate?: ")
#     betweenNumbersCheck = input('Would you like to integrate between two points?: ')
#     if betweenNumbersCheck == 'yes':
#         doesWantToIntegrateBetweenPoints = True
#         inputPoints = input('What are the 2 points (Please separate each by a comma): ')
#         return [expressionInput, inputPoints]
#     else:
#         return [expressionInput, '']


def divide():
    """
    This function take in a given expression from a user and extends a list with each valid expression separating
    out each expression.
    It then returns that dissected string as a list
    :return: dissected string as a list
    """
    # Check what number to integrate
    userInputTwo = input("Integrate what expression: ")
    # The list to be returned
    compositeList = []
    # This string collects all valid character, (i.e not + or -)
    inputString = ''
    # Break input into separate parts
    readOperations = False
    # Look at all characters in a list
    for cha in userInputTwo:
        # This will read a negative sign in a bracket
        if cha == '(':
            readOperations = True
            inputString += cha
        elif cha == ')':
            readOperations = False
            inputString += cha
        elif readOperations:
            inputString += cha
        # For all other valid characters
        elif (cha != '') and cha not in operationList:
            inputString += cha
        else:
            # If an operation, append the list with the sub expression
            compositeList.append(inputString)
            compositeList.append(cha)
            inputString = ''
    compositeList.append(inputString)
    return compositeList


def classifyIntegrals(inputList):
    """
    This function looks at the sub expressions of a given expression and classifies how to integrate them.
    It will return a list of commands that whose index corresponds with their respective expression in the expression
    list
    :param inputList: A list of expressions created by the original input
    :return: a list of strings of commands for each expression
    """
    # This is a boolean that will allow the reader to read negative signs
    readOperations = False
    # This is a list that will
    commandList = []
    # This is to be used to determine if an expression is just a simple one, i.e like 5x
    finishedLooking = False
    natural_log_trigger = False
    integral = ''
    trigHolder = ''
    readTrig = False
    for expressions in inputList:
        # If the expression is an operation, ignore it
        if expressions in operationList:
            commandList.append('ignore')
        else:
            for cha in expressions:
                # If there is an e within the expression, it is probably an exponential function
                if cha == 'e':
                    commandList.append('exponential')
                    finishedLooking = True
                    break
                # If the followings characters are signs of trig's
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
                # This is to read negative signs
                elif cha == '(':
                    readOperations = True
                elif cha == ')':
                    readOperations = False
                # If the character is a -, then expect the possibility of a natural log
                elif cha == '-' and readOperations:
                    natural_log_trigger = True
                # If the natural log trigger is on and the character is 1, then the expression will become a
                # natural log
                elif natural_log_trigger and cha == '1':
                    commandList.append('naturalLog')
                    finishedLooking = True
                    break
            # If no unique character is found, it is assumed to be a simple expression
            if not finishedLooking:
                commandList.append('simple')
    return commandList


def allocateIntegration(expressionList, commandList):
    """
    This function sends each expression into their respective integration calculator based of what the command list
    says. The original list is returned with the new expressions
    :param expressionList: The list of expressions to be integrated
    :param commandList: The list of commands
    :return: The original expression list, but with integrated terms
    """
    # Counts how many times each expression has been integrated
    countOfIntegrals: int = 0
    # While the count is less than the length of the list, assign the expressions to their calculator
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
    """
    This calculator will try to integrate and return a simple expression
    :param inputExpression: A expression of some function represented as a string
    :return: The above integrated expression
    """
    # This will be used to put brackets round a negative expression later
    recordIfNegative = False
    # This is to tell if the expression isn't just some constant
    noPower = True
    # This holds the coefficient of the expression
    numberString = ""
    readBool = False
    # This holds the power value to later multiply the coefficient with
    multiplier = ""
    # Extract the front coefficient
    for numbers in inputExpression:
        if numbers != "x":
            numberString += numbers
        else:
            noPower = False
            break
    # If the expression is just a constant, return it + the variable
    if noPower:
        return numberString + 'x'
    # This scan reads the content of the power
    # It will start analysing the expression once it sees the ^ sign and records it in multiplier
    for cha in inputExpression:
        if cha == '^':
            readBool = True
        elif readBool:
            # Only read the character if it is in within a bracket
            if cha != '(' and cha != ')':
                multiplier += cha
            # To tell if the power is a negative
            if cha == '-':
                recordIfNegative = True

    # The below code add a number to the power, divides the coefficient by the new power,
    # then reconstructs the new expression and adds it back to the list
    multiplier = float(multiplier) + 1
    newFront = float(numberString) / multiplier
    if recordIfNegative:
        inputExpression = str(newFront) + 'x^(' + str(multiplier) + ')'
    else:
        inputExpression = str(newFront) + 'x^' + str(multiplier)
    return inputExpression


def integrateByParts():
    """
    This will be used to solve an integration problem where it is integration by parts
    :return:
    """
    pass


def exponentialIntegration(inputExpression):
    """
    This calculator will try to integrate and return an exponential expression
    :param inputExpression: A expression of some function represented as a string
    :return: The above integrated expression
    """
    # This holds the coefficient of the expression
    numberString = ""
    readBool = False
    # This holds the power value to later multiply the coefficient with
    multiplier = ""
    # Extract the front coefficient
    for numbers in inputExpression:
        if (numbers != "e"):
            numberString += numbers
        else:
            break
    # If the expression is just e...
    if numberString == '':
        numberString = '1'
    # This scan reads the power
    for cha in inputExpression:
        # If the character is ^, start reading
        if cha == '^':
            readBool = True
        elif readBool:
            # If there is a variable expression
            if cha == 'x':
                break
            # Read the insides of the bracket
            if cha != '(' and cha != ')':
                multiplier += cha

    # The below code add a number to the power, divides the coefficient by the new power, then reconstructs the new
    # expression and adds it back to the list
    multiplier = int(multiplier)
    newFront = int(numberString) / multiplier
    inputExpression = str(newFront) + 'e^(' + str(multiplier) + 'x)'
    return inputExpression


def integrateTrig(inputExpression):
    """
    This calculator will try to integrate and return a trig expression
    :param inputExpression: A expression of some function represented as a string
    :return: The above integrated expression
    """
    # The coefficient
    frontString = ''
    # The coefficient multiplying the variable
    trigString = ''
    # The other half of the expression, other than the front coefficient
    endString = ''
    # The expression within the bracket
    bracketString = ''
    readBracket = False
    # The boolean to tell the below reader to read the coefficient
    readFront = True
    # This reader will divide the expression into the coefficient and the trig
    for numbers in inputExpression:
        if numbers.isdigit() and readFront:
            frontString += numbers
        else:
            endString += numbers
            readFront = False
    # This reader will find the expression in the bracket
    for cha in endString:
        # Exist once reached the variable
        if cha == 'x':
            break
        # Read the contents within the bracket
        elif cha != '(' and not readBracket:
            trigString += cha
        elif readBracket:
            bracketString += cha
        else:
            readBracket = True

    # If the bracket and coefficient expression are empty
    if bracketString == '':
        bracketString = 1
    if frontString == '':
        frontString = 1
    # The new front
    newFront = str(int(frontString) / int(bracketString))
    # Express the expressions as strings
    if newFront == '1.0':
        newFront = ''
    if bracketString == 1:
        bracketString = ''
    # Integrate the actual trig parts
    if trigString == 'cos':
        return newFront + 'sin(' + str(bracketString) + 'x)'
    elif trigString == 'sin':
        return '-' + newFront + 'cos(' + str(bracketString) + 'x)'


def integrationByNaturalLog(inputExpression):
    """
    This calculator will try to integrate and return a natural log expression
    :param inputExpression: A expression of some function represented as a string
    :return: The above integrated expression
    """
    # The front coefficient
    numberString = ""
    # The power number
    variableString = ""
    readExpressionBracket = False
    # The below for loop reads the coefficient at the front
    for numbers in inputExpression:
        if numbers != "x" and numbers != '(':
            numberString += numbers
        else:
            break
    # This reader will read the expression in the brackets of the power
    for numbers in inputExpression:
        if numbers == '(':
            readExpressionBracket = True
        elif numbers == ')':
            break
        elif readExpressionBracket:
            variableString += numbers
    return numberString + 'ln(' + variableString + ')'


def rebuild(inputList):
    """
    This function will analyse a list of integrated expressions and combine the list to return a string
    :param inputList: A list of expression(s)
    :return: A string of expression(s)
    """
    returnString = ''
    for expressions in inputList:
        returnString += expressions + ' '
    return returnString


def oneVariable():
    """
    This is the function where the integration happens
    :return: A integrated expression
    """
    # Read the input and divide the expressions
    processedInputList = divide()
    # Assign the commands for each sub expression
    commandList = classifyIntegrals(processedInputList)
    # Integrate each sub expression
    allocateIntegration(processedInputList, commandList)
    # Return the integrated expression
    return rebuild(processedInputList)
