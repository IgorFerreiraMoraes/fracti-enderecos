import sys

sys.path.append("../")
from fracti import split_address

import unittest


class TestSplitAdrres(unittest.TestCase):
    # Casos Simples
    def test_simple_case_a(self):
        address_input = "Miritiba 339"
        expected_output = {"Miritiba", "339"}
        self.assertEqual(split_address(address_input), expected_output)

    def test_simple_case_b(self):
        address_input = "Babaçu 500"
        expected_output = {"Babaçu", "500"}
        self.assertEqual(split_address(address_input), expected_output)

    def test_simple_case_c(self):
        address_input = "Cambuí 804B"
        expected_output = {"Cambuí", "804B"}
        self.assertEqual(split_address(address_input), expected_output)

    # Casos Mais Complicados
    def test_complex_case_a(self):
        address_input = "Rio Branco 23"
        expected_output = {"Rio Branco", "23"}
        self.assertEqual(split_address(address_input), expected_output)

    def test_complex_case_b(self):
        address_input = "Quirino dos Santos 23 b"
        expected_output = {"Quirino dos Santos", "23 b"}
        self.assertEqual(split_address(address_input), expected_output)

    def test_complex_case_c(self):
        address_input = "Rua 25 de Março 23a"
        expected_output = {"Rua 25 de Março", "23a"}
        self.assertEqual(split_address(address_input), expected_output)

    # Casos Internacionais
    def test_international_case_a(self):
        address_input = "4, Rue de la République"
        expected_output = {"Rue de la République", "4"}
        self.assertEqual(split_address(address_input), expected_output)

    def test_international_case_b(self):
        address_input = "100 Broadway Av"
        expected_output = {"Broadway Av", "100"}
        self.assertEqual(split_address(address_input), expected_output)

    def test_international_case_c(self):
        address_input = "Calle Sagasta, 26"
        expected_output = {"Calle Sagasta", "26"}
        self.assertEqual(split_address(address_input), expected_output)

    def test_international_case_d(self):
        address_input = "Calle 44 No 1991"
        expected_output = {"Calle 44", "No 1991"}
        self.assertEqual(split_address(address_input), expected_output)


if __name__ == "__main__":
    unittest.main()
