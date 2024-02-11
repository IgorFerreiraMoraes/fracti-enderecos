import re


def split_address(input_address):
    # Expressões regulares para identificar diferentes formatos de endereço
    patterns = {
        "indicator_street": r"^(.*?)(?=,?\s(?:No|n°|number)\s*\d+$)",
        "indicator_number": r"(?:No|n°|number)\s*\d+$",
        "national_street": r"^(.*?)(?=,?\s\d+\s*[a-zA-Z]?\b$)",
        "national_number": r"(\d+\s*[a-zA-Z]?\b)$",
        "inverted_street": r"^\d+\s*[a-zA-Z]?\b[,]?\s*",
        "inverted_number": r"^(\d+(\s*[a-zA-Z]\b)?)(?=,?\s*\w)",
    }

    # Verifica o formato do endereço e extrai a rua e o número correspondentes
    if re.search(patterns["indicator_street"], input_address) and re.search(
        patterns["indicator_number"], input_address
    ):
        street = re.search(patterns["indicator_street"], input_address).group()
        number = re.search(patterns["indicator_number"], input_address).group()
    elif re.search(patterns["national_street"], input_address) and re.search(
        patterns["national_number"], input_address
    ):
        street = re.search(patterns["national_street"], input_address).group()
        number = re.search(patterns["national_number"], input_address).group()
    elif re.search(patterns["inverted_street"], input_address) and re.search(
        patterns["inverted_number"], input_address
    ):
        street = re.split(patterns["inverted_street"], input_address)[1]
        number = re.search(patterns["inverted_number"], input_address).group()
    else:
        return "Não foi possível processar o endereço"

    address_parts = [street, number]
    return address_parts


def main():
    address = input("Insira Um Endereço:\n")
    parts = split_address(address)

    print(parts)

    input("Aperte qualquer tecla para sair...")


if __name__ == "__main__":
    main()
