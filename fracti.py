import re

def split_address(input_address):
    # Expressões regulares para identificar diferentes formatos de endereço
    national_street_pattern = r'^.*?(?=[,]?\s\d+\s*[a-zA-Z]?\b$)'
    national_number_pattern = r'(\d+\s*[a-zA-Z]?\b)$'
    
    indicator_street_pattern = r'^.*?(?=[,]?\s((?:No|n°|number)\s*\d+)$)'
    indicator_number_pattern = r'(?:No|n°|number)\s*\d+$'

    inverted_number_pattern = r'^\d+(\s*[a-zA-Z]\b)?(?=[,]?\s*\w)'
    inverted_street_pattern = r'^\d+\s*[a-zA-Z]?\b[,]?\s*'

    # Verifica o formato do endereço e extrai a rua e o número correspondentes
    if re.search(indicator_street_pattern, input_address) and re.search(indicator_number_pattern, input_address):
        street = re.search(indicator_street_pattern, input_address).group()
        number = re.search(indicator_number_pattern, input_address).group()
    elif re.search(national_street_pattern, input_address) and re.search(national_number_pattern, input_address):
        street = re.search(national_street_pattern, input_address).group()
        number = re.search(national_number_pattern, input_address).group()
    elif re.search(inverted_street_pattern, input_address) and re.search(inverted_number_pattern, input_address): 
        street = re.split(inverted_street_pattern, input_address)[1]
        number = re.search(inverted_number_pattern, input_address).group()
    else:
        return 'Não foi possível processar o endereço'

    address_parts = [street, number]
    return address_parts

def main():
    address = input('Insira Um Endereço:\n')
    parts = split_address(address)

    print(parts)

    input('Aperte qualquer tecla para sair...')

if __name__ == "__main__":
    main()
