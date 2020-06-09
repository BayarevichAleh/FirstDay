def rank(x, n):
    """
    Finding sqrt
    :param x: number
    :type x: int
    :param n: rank
    :type n: int
    :return: sqrt
    """
    rank = 1
    for i in range(n):
        rank = rank * x
    return rank


x = int(input("Enter x:"))
y = (rank(x, 6) * rank(x - 5, 3)) / rank(2 * x + 1, 5)
print(y)
