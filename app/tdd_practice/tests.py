"""
Sample tests
"""

from django.test import TestCase
from django.test import SimpleTestCase
from .views import view_add
from .calculator import Calculator


# Create your tests here.

# TEST 1 : calculator -> NOW WORKING GOOD !!
class CalcTests(SimpleTestCase):
    """Test the calculator module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        # Create Calculator object
        calculator_1 = Calculator()

        res = calculator_1.add(10, 9)
        self.assertEqual(res, 19)


# TEST 2 : Just do test code without module import
class NoModuleTests(SimpleTestCase):
    """Check out whether Django test work or not"""

    def test_assert_equal_01(self):
        """Test assertEqual with integer variable and number """

        res = 3 + 5
        self.assertEqual(res, 8)


# TEST 3 : Import "views.py" module
# -> Working
# -> from 으로는 .py 파일을 가져오고 import 로 함수 또는 클래스를 가져와야 동작 함
class ViewsTests(SimpleTestCase):
    """Check out whether Django can import initial modules or not """

    def test_view_assert_equal_01(self):
        """Test Simple add method from views.py"""

        res = view_add(10, 7)
        self.assertEqual(res, 17)
