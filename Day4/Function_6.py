def dec_to_hex(number):
    """
    Сonversion DECIMAL to HEX
    :param number: decimal-number
    :type number: int
    :return: hex-number
    """
    hex_number = ""
    hex_literal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    while number > 0:
        hex_number = f'{hex_literal[number & 15]}{hex_number}'
        number = number >> 4
    hex_number = f'0x{hex_number}'
    return hex_number


number = int(input("Enter decimal number:"))
print(f'User function:{dec_to_hex(number)}')
print(f'Standart function:{hex(number)}')
