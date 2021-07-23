

# One variable:
from integrator.Integrator_One_variable import oneVariable


def integrator():

    userInput = input("How many variables?: ")
    processedUserInput = checker(userInput)

    if processedUserInput == '1':
        returnStmnt = oneVariable() + '+ Constant'
        return returnStmnt

    elif processedUserInput == '2':
        pass

    elif processedUserInput == '3':
        pass

    else:
        print('invalid statement try again')

def checker(inputStr):

    # If input is one
    checkListOne = [1,"one","One","ONE","1"]
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


