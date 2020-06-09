def number_expansion(a):
    """
    Number expansion
    :param a: number
    :type a: int
    :return: list of dividers
    """
    number_expansion = list()
    while a > 1:
        for j in range(2, a + 1):
            if a % j == 0:
                a = int(a / j)
                number_expansion.append(j)
                break
    return number_expansion


def gcd(a, b):
    """
    Finding gcd
    :param a: number 1
    :param b: number 2
    :type a, b: int
    :return: gcd a and b
    """
    expansion_a = number_expansion(a)
    expansion_b = number_expansion(b)
    gcd = 1
    for i in expansion_a:
        if i in expansion_b:
            gcd *= i
            expansion_b.remove(i)
    return gcd

number_1 = int(input("Enter number 1:"))
number_2 = int(input("Enter number 2:"))
print(f'GCD equals: {gcd(number_1,number_2)}')
