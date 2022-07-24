"""
Sample tests
"""

from django.test import TestCase
from django.test import SimpleTestCase

# Create your tests here.


# calculator.py test
import calculator


class CalcTests(SimpleTestCase):
    """Test the calculator module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calculator.add(9, 10)
        self.assertEqual(res, 19)
