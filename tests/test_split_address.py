import sys

sys.path.append("../")
from fracti import split_address

import unittest


class TestSplitAdrres(unittest.TestCase):
    test_cases = [  # Tuplas com a entrada e saída esperada
        ("Miritiba 339", ["Miritiba", "339"]),
        ("Babaçu 500", ["Babaçu", "500"]),
        ("Cambuí 804B", ["Cambuí", "804B"]),
        ("Rio Branco 23", ["Rio Branco", "23"]),
        ("Quirino dos Santos 23 b", ["Quirino dos Santos", "23 b"]),
        ("Rua 25 de Março 23a", ["Rua 25 de Março", "23a"]),
        ("4, Rue de la République", ["Rue de la République", "4"]),
        ("100 Broadway Av", ["Broadway Av", "100"]),
        ("Calle Sagasta, 26", ["Calle Sagasta", "26"]),
        ("Calle 44 No 1991", ["Calle 44", "No 1991"]),
    ]

    def run_test(self, address_input, expected_output):
        result = split_address(address_input)
        print(
            f"Input: {address_input}\n Expected Output: {expected_output}\n Actual Output:   {result}\n"
        )
        self.assertEqual(result, expected_output)

    def test_all_cases(self):
        for address_input, expected_output in self.test_cases:
            self.run_test(address_input, expected_output)
        input("Aperte enter para sair...")


if __name__ == "__main__":
    unittest.main()
