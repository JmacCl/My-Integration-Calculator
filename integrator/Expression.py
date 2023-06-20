"""
This file contains information on the Expression class

A mathematical expression is made up of multiple artifacts like 5x^4x + 1, in which 5x and 1 are the
artifacts seperated by the operator +

"""
from typing import List

import Artifact


class Expression:

    def __int__(self, input_exp: str, command: str):
        expression = self.generate_expression(self, input_exp=input_exp)
        self.expression = expression
        if command == 'differentiate':
            self.differentiate(self, self.expression)
        elif command == ' integrate':
            self.integrate(self, self.expression)

    def generate_expression(self, input_exp: str):
        return ''

    def simplify(self):
        """
        Change Expression object to a simpler Expression object. SImple is meant to indicate easier to integrate.
        :return:
        """
        pass

    def differentiate(self, expression):
        pass

    def integrate(self, expression):
        expression.integrate()


