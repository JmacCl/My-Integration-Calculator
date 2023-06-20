import unittest
import integrator.integrator_old
from unittest.mock import patch


class TestSingleTerms(unittest.TestCase):
    """Test function with one variable and just one term"""

    def testIntegratesSingleVariable(self):
        user_Input = ['1', '5x^(4)']
        expected_Output = '1.0x^5.0 + Constant'

        with patch('builtins.input', side_effect=user_Input):
            integral = integrator.Integrator.integrator()

        self.assertEqual(integral, expected_Output)

    def testIntegratorWithOneTernToThePowerOfNegative(self):
        user_Input = ['1', '5x^(-2)']
        expected_Output = str(-5 / 1) + 'x^(-1.0) + Constant'

        with patch('builtins.input', side_effect=user_Input):
            integral = integrator.Integrator.integrator()

        self.assertEqual(integral, expected_Output)

    def testIntegratorWithOneTernToThePowerOfNegativeOne(self):
        user_Input = ['1', '5(x)^(-1)']
        expected_Output = '5ln(x) + Constant'

        with patch('builtins.input', side_effect=user_Input):
            integral = integrator.Integrator.integrator()

        self.assertEqual(integral, expected_Output)

    def testSingleExponential(self):
        user_Input = ['1', 'e^(4x)']
        expected_Output = '0.25e^(4x) + Constant'

        with patch('builtins.input', side_effect=user_Input):
            integral = integrator.Integrator.integrator()
        self.assertEqual(integral, expected_Output)

    def testIntegratesSingleVariableNoPower(self):
        user_Input = ['1', '7']
        expected_Output = '7x + Constant'

        with patch('builtins.input', side_effect=user_Input):
            integral = integrator.Integrator.integrator()

        self.assertEqual(integral, expected_Output)

    def testWithPowerFraction(self):
        user_Input = ['1', '6x^0.5']
        expected_Output = '4.0x^1.5 + Constant'

        with patch('builtins.input', side_effect=user_Input):
            integral = integrator.Integrator.integrator()

        self.assertEqual(integral, expected_Output)

    def testNaturalLogWithExpression(self):
        user_Input = ['1', '(x-4)^(-1)']
        expected_Output = 'ln(x-4) + Constant'

        with patch('builtins.input', side_effect=user_Input):
            integral = integrator.Integrator.integrator()

        self.assertEqual(integral, expected_Output)

    def testIntegrationWithCosine(self):
        user_Input = ['1', 'cos(x)']
        expected_Output = 'sin(x) + Constant'

        with patch('builtins.input', side_effect=user_Input):
            integral = integrator.Integrator.integrator()

        self.assertEqual(integral, expected_Output)

    def testIntegrationWithSine(self):
        user_Input = ['1', 'sin(x)']
        expected_Output = '-cos(x) + Constant'

        with patch('builtins.input', side_effect=user_Input):
            integral = integrator.Integrator.integrator()

        self.assertEqual(integral, expected_Output)

    def testIntegrationWithBasicTrigSine(self):
        user_Input = ['1', '6sin(2x)']
        expected_Output = '-3.0cos(2x) + Constant'

        with patch('builtins.input', side_effect=user_Input):
            integral = integrator.Integrator.integrator()

        self.assertEqual(integral, expected_Output)

    def testIntegrationWithBasicTrigCosine(self):
        user_Input = ['1', '6cos(3x)']
        expected_Output = '2.0sin(3x) + Constant'

        with patch('builtins.input', side_effect=user_Input):
            integral = integrator.Integrator.integrator()

        self.assertEqual(integral, expected_Output)


class TestMultipleExpressions(unittest.TestCase):
    """Test function with one variable and two terms
    separated by + """

    def testIntegratorWithTwoTermsSeparatedByAddition(self):
        user_Input = ['1', '5x^(4) + 32x^(15)']
        expected_Output = '1.0x^5.0 + 2.0x^16.0 + Constant'

        with patch('builtins.input', side_effect=user_Input):
            integral = integrator.Integrator.integrator()

        self.assertEqual(integral, expected_Output)

    '''Test function with one variable and two terms
    separated by - '''

    def testIntegratorWithTwoTermsSeparatedBySubtraction(self):
        user_Input = ['1', '5x^(4) - 32x^(15)']
        expected_Output = '1.0x^5.0 - 2.0x^16.0 + Constant'

        with patch('builtins.input', side_effect=user_Input):
            integral = integrator.Integrator.integrator()

        self.assertEqual(integral, expected_Output)


if __name__ == '__main__':
    unittest.main()
