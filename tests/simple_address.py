import sys
sys.path.append('../')
from fracti import split_address

import unittest

class TestSimpleCase(unittest.TestCase):
    def test_case_a(self):
        address_input = 'Miritiba 339'
        expected_output = ['Miritiba', '339']
        self.assertEqual(split_address(address_input), expected_output)
    def test_case_b(self):
        address_input = 'Babaçu 500'
        expected_output = ['Babaçu', '500']
        self.assertEqual(split_address(address_input), expected_output)
    def test_case_c(self):
        address_input = 'Cambuí 804B'
        expected_output = ['Cambuí', '804B']
        self.assertEqual(split_address(address_input), expected_output)

if __name__ == '__main__':
    unittest.main()
