import unittest
from unittest.mock import patch


class TestLatexInput(unittest.TestCase):
    """Test function with one variable and just one term"""

    def test_simple_latex_expression(self):
        user_Input = ['1', '$5x^{4}$']
        expected_Output = '1.0x^5.0 + Constant'

        with patch('builtins.input', side_effect=user_Input):
            integral = integrator.Integrator.integrator()

        self.assertEqual(integral, expected_Output)


if __name__ == '__main__':
    unittest.main()
