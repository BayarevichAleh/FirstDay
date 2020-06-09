def registr(world):
    """
    :param world: input world
    :type world: string
    :return: changed world
    """
    up = 0
    down = 0
    if world.isalpha():
        for i in world:
            if i.isupper():
                up += 1
            else:
                down += 1
        if up > down:
            return world.upper()
        else:
            return world.lower()

    else:
        return  "Incorrect data"

while True:
    user_world = input("Enter world:")
    print(registr(user_world))