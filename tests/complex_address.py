import sys

sys.path.append("../")
from fracti import split_address

import unittest


class TestComplexCase(unittest.TestCase):
    def test_case_a(self):
        address_input = "Rio Branco 23"
        expected_output = ["Rio Branco", "23"]
        self.assertEqual(split_address(address_input), expected_output)

    def test_case_b(self):
        address_input = "Quirino dos Santos 23 b"
        expected_output = ["Quirino dos Santos", "23 b"]
        self.assertEqual(split_address(address_input), expected_output)

    def test_case_c(self):
        address_input = "Rua 25 de Março 23a"
        expected_output = ["Rua 25 de Março", "23a"]
        self.assertEqual(split_address(address_input), expected_output)


if __name__ == "__main__":
    unittest.main()
