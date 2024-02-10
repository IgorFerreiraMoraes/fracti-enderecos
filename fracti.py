import re

def split_address(address):
    number_expression = r'(\d+\s*[a-zA-Z]?\b)$'
    """
    \d+ Encontra um ou mais dígitos
    \s* Identifica zero ou mais espaços
    [a-zA-Z]?\b Corresponde a uma letra (minúscula ou maiúscula) opcional
    $ Garante que o número está no fim do endereço
    """
    
    street_expression = r'^.*?(?=\s\d+\s*[a-zA-Z]?\b$)'
    """
    ^ Começa o match no inicio da linha
    .*? Encontra todos os caracteres até a próxima parte da expressão ser satisfeita
    (?=\s...) Verifica se a posição atual é seguida por um espaço em branco e depois pelo número \d+\s*[a-zA-Z]?\b
    """

    street_match = re.match(street_expression, address)
    number_search = re.search(number_expression, address)

    street = street_match.group() if street_match else None # Checa o padrão no começo da linha
    number = number_search.group() if number_search else None # Checa o padrão em qualquer parte
    address_parts = [street, number]

    return address_parts

def main():
    address = input('Insira Um Endereço:\n')
    parts = split_address(address)

    print(parts)

    input('Aperte qualquer tecla para sair...')

if __name__ == "__main__":
    main()
