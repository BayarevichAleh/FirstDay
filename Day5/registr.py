up = 0
down = 0

while True:
    world = input("Enter world:")
    if world.isalpha():
        for i in world:
            if i.isupper():
                up += 1
            else:
                down += 1
        if up > down:
            print(world.upper())
        else:
            print(world.lower())

    else:
        print("Incorrect data")
