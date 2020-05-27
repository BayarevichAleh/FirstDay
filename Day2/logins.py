input_login = input("Enter your login:")
if len(input_login) > 0 and len(input_login) < 11:
    if input_login[0:2] == "io":
        if input_login[2:len(input_login)].isdecimal():
            print("Correct")
        else:
            print("Incorrect")
    else:
        print("Incorrect")
else:
    print("Incorrect")
