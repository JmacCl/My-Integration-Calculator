"""
Class to represent each possible mathematical artifacts, like 1, 2, 5x
"""
class Artifacts:


    def __int__(self, coefficient, variable, power):
        self.__validify_inputs(coefficient, variable, power)
        self.coefficient = coefficient
        self.variable = variable
        self.power = power

    def simplify_artifact(self):
        pass

    def __validify_inputs(self, coefficient, variable, power):
        pass

