# https://github.com/turtle1won/lab11-AP-NR.git
# Partner 1: Aditya Patel
# Partner 2: Nyden Rodewald

import unittest
from calculator import *

#

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 5), 7)
        self.assertEqual(add(3, -5), -2)
        self.assertAlmostEqual(add(-1.3, 4.7), 3.4)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(2, 5), -3)
        self.assertEqual(subtract(3, -5), 8)
        self.assertAlmostEqual(subtract(-1.3, 4.7), -6.0)
        

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code
    def test_multiply(self):
        self.assertEqual(mul(2,3), 6)
        self.assertEqual(mul(-4,4),-16)
        self.assertEqual(mul(-2,-3),6)


    # def test_divide(self): # 3 assertions
    #     fill in code

    def test_divide(self):
        self.assertEqual(div(3,6), 2)
        self.assertEqual(div(-4,4),-1)
        self.assertAlmostEqual(div(3,2),.67,places = 2)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 8), 3.0)
        self.assertEqual(logarithm(3, 9), 2.0)
        self.assertAlmostEqual(logarithm(16, 64), 1.5)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_log_ivalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(5, -1)

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(5,12), 13)
        self.assertEqual(hypotenuse(-8,-15),17)
    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code


    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-36)
        self.assertEqual(square_root(36),6)
        self.assertEqual(square_root(25),5)

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()