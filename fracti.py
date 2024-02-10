def split_address(address):
    address_parts = address.split()
    return address_parts

def main():
    address = input('Insira Um Endereço:\n')
    parts = split_address(address)

    print(parts)

    input('Aperte qualque tecla para sair...')

if __name__ == "__main__":
    main()
