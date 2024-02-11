import re


# Expressões regulares para identificar diferentes formatos de endereço
patterns = {
    "indicator_street": r"^(.*?)(?=,?\s(?:No|n°|number)\s*\d+$)",
    "indicator_number": r"(?:No|n°|number)\s*\d+$",
    "national_street": r"^(.*?)(?=,?\s\d+\s*[a-zA-Z]?\b$)",
    "national_number": r"(\d+\s*[a-zA-Z]?\b)$",
    "inverted_street": r"^\d+\s*[a-zA-Z]?\b[,]?\s*",
    "inverted_number": r"^(\d+(\s*[a-zA-Z]\b)?)(?=,?\s*\w)",
}


def split_address(input_address):
    address_parts = set()

    # Verifica o formato do endereço e extrai a rua e o número correspondentes
    for pattern_name, pattern_expression in patterns.items():
        match = re.search(pattern_expression, input_address)
        if pattern_name == "inverted_street":  # Diferente com número no começo
            match = re.search(
                re.split(pattern_expression, input_address)[1], input_address
            )
        if match:
            address_parts.add(match.group())
            if (
                len(address_parts) == 2
            ):  # Dois itens, rua e número, não é necessário continuar o loop
                break

    return address_parts


def main():
    address = input("Insira Um Endereço:\n")
    parts = split_address(address)

    print(parts)

    input("Aperte qualquer tecla para sair...")


if __name__ == "__main__":
    main()
