import unittest
from app import  addition
from multiply import multiply

class AdditionTestCase(unittest.TestCase):
    def test_main(self):
        result = addition(3,2)
        assert result == 5

    def test_three_args(self):
        result = addition(3,2,1)
        assert result == 6

    def test_no_args(self):
        result = addition()
        assert result == 0

    def test_multiply_3_args(self):
        result = multiply(13,2)
        assert result == 26

if __name__ == '__main__':
    unittest.main()
