def sort_world(string):
    """
    Sorting worlds in a string
    :param string: text
    :type string: str
    :return: sorted text
    """
    string = string.split()
    sort_string = ""
    for i in range(len(string)):
        string[i] = ''.join(sorted(string[i]))
        sort_string = f'{sort_string} {string[i]}'
    return sort_string


string = input("Enter string:")
print(sort_world(string))
