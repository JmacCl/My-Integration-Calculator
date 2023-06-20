from integrator.Expression import Expression
import argparse
import os

def process_file_input(file_location):
    pass

def main(expression_input, command, file_location = None):
    if file_location:
        process_file_input(expression_input)

    # Generate Expression
    exp = Expression(expression_input, command)




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Integrate/Differentiate a given expression')
    parser.add_argument('expression_input', type=str, help='Input of the integral expression one wants to input')
    parser.add_argument('command', type=str, help='Specify differentiation or integration')
    parser.add_argument('--file_location', type=str, help='If wanting to use a file location to integrate the expression')
    args = parser.parse_args()
    main()



'''

All the steps for the integration calculator to be completed: 

(bare in mind, tests must be done for each step)

Single Integral
1. Integrate simple terms: 56x^55 (DONE)
2. integrate multiple terms separated by + and -: 56x^55 + 42x^5 - 54x^7 (Done)
3. Integrate simple Trig and hyperbolic (sinx, cosx, sinhx,coshx)
4. Integrate Other math terms: (e^x, 1/x^(something))
5. Integration by parts 

Other implementations:
1. Being able to integrate between two numbers,
2. Being able to integrate multiple variables. 
3. being able to input strings, latex code and pdf of terms
4. differentiation
'''