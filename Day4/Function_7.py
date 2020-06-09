def dec_to_bin_oct(number, sistem):
    """
    Сonversion DECIMAL to BINARY or OCTAL
    :param number: decimal number
    :param sistem: sistem (May be "bin","BIN","oct","OCT")
    :return: binary or octal number
    """
    if sistem == "bin" or sistem == "BIN":
        bin_number = ""
        while number > 0:
            bin_number = f'{number & 1}{bin_number}'
            number = number >> 1
        return f'0b{bin_number}'
    elif sistem == "oct" or sistem == "OCT":
        oct_number = ""
        while number > 0:
            oct_number = f'{number & 7}{oct_number}'
            number = number >> 3
        return f'0o{oct_number}'
    else:
        return "Incorect data"


number = int(input("Enter decimal number:"))
sistem = input("Enter sistem:")
print(f'User function:{dec_to_bin_oct(number, sistem)}')

if sistem == "bin" or sistem == "BIN":
    print(f'Sistem function: {bin(number)}')
elif sistem == "oct" or sistem == "OCT":
    print(f'Sistem function: {oct(number)}')
else:
    print("Sistem function: Incorect data")

