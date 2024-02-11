import sys

sys.path.append("../")
from fracti import split_address

import unittest


class TestInternationalCase(unittest.TestCase):
    def test_case_a(self):
        address_input = "4, Rue de la République"
        expected_output = ["Rue de la République", "4"]
        self.assertEqual(split_address(address_input), expected_output)

    def test_case_b(self):
        address_input = "100 Broadway Av"
        expected_output = ["Broadway Av", "100"]
        self.assertEqual(split_address(address_input), expected_output)

    def test_case_c(self):
        address_input = "Calle Sagasta, 26"
        expected_output = ["Calle Sagasta", "26"]
        self.assertEqual(split_address(address_input), expected_output)

    def test_case_d(self):
        address_input = "Calle 44 No 1991"
        expected_output = ["Calle 44", "No 1991"]
        self.assertEqual(split_address(address_input), expected_output)


if __name__ == "__main__":
    unittest.main()
