# One variable:
from integrator.Integrator_One_variable import oneVariable


def integrator() -> str:
    """
    This function takes in an expression to be integrated, and returns the integrated expression.

    :return:
    String: the integrated expression
    """

    # Take in user input of how many variables they would like to integrate
    userInput = input("How many variables?: ")
    processedUserInput = checker(userInput)

    # If user would like to use just one variable
    if processedUserInput == '1':
        returnStmt = oneVariable() + '+ Constant'
        return returnStmt

    # If user would like to use two...
    elif processedUserInput == '2':
        pass

    # If user would like to use three...
    elif processedUserInput == '3':
        pass

    # If all else fails, break out and print the following statement
    else:
        print('invalid statement try again')
        return "ERROR"


def checker(inputStr: str) -> str:
    """
    This function checks that a given input is valid, and will
    :param inputStr: The string that is needing to be tested
    :return: The processed version of the input string
    """

    # If input is one
    checkListOne = [1, "one", "One", "ONE", "1"]
    if inputStr in checkListOne:
        return '1'

    # If input is two
    checkListTwo = [2, "two", "Two", "TWO", "2"]
    if inputStr in checkListTwo:
        return '2'

    # If input is three
    checkListThree = [3, "three", "Three", "THREE", "3"]
    if inputStr in checkListThree:
        return '3'

    return "ERROR"
