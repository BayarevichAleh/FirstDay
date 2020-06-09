def move_to(a: list, n: int, route: str):
    """
    Move list to right or left on n positions
    :param a: list
    :param n: how much positions
    :param route: route right - '>' or left - '<'
    :return: moved list
    """
    for i in range(n):
        if route == ">":
            a.insert(0, a.pop())
        elif route == "<":
            a.insert(len(a) - 1, a.pop(0))
    return a


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
number = int(input("Enter how much of position to move:"))
route = input("Enter route '<' or '>':")
print(move_to(a, number, route))

