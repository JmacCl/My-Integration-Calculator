"""
This file contains information on the Expression class

A mathematical expression is made up of multiple artifacts like 5x^4x + 1, in which 5x and 1 are the
artifacts seperated by the operator +

"""
from typing import List

import Artifact


class Expression:

    def __int__(self, input: str, expression, artifacts, command: str):
        self.expression = self.generate_expression(self, input=input)
        if command == 'differentiate':
            self.differentiate(self, expression)
        elif command == ' integrate':
            self.integrate(self, expression)

    def generate_expression(self, input: str):
        print(input)

    def simplify(self):
        """
        Change Expression object to a simpler Expression object. SImple is meant to indicate easier to integrate.
        :return:
        """
        pass

    def differentiate(self, expression):
        pass

    def integrate(self, expression):
        pass


