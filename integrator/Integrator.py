from integrator import Expression, Artifact

class Integrator:

    def __init__(self, old_expression: Artifact):
        self.raw_expression = old_expression
        self.result_expression = self.allocate_integration(self.raw_expression)


    def allocate_integration(self, art):
        return self.integrate(art)

    def integrate_by_sub(self):
        pass

    def integrate_by_parts(self):
        pass

    def integrate_trig(self):
        pass

    def integrate(self, art: Artifact):

        new_power = art.power + 1
        new_coefficient = art.coefficient/new_power

        return Artifact(new_power, new_coefficient)




