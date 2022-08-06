while True:
    sequencelist = []
    # Get user input and validate for positive integer
    while True:
        try:
            usernum = int(input("Please enter a positive integer: "))
        except ValueError:
            print("Please enter an integer in numerical format")
            continue
        if usernum < 1:
            print("Please enter a valid number")
        else:
            break

    # if user input is odd multiply by 3 and add 1 and if even number divide by 2, repeat until 1 is reached
    while usernum > 1:
        if usernum % 2 != 0:
            usernum = (usernum * 3) + 1
        elif usernum % 2 == 0:
            usernum /= 2
        sequencelist.append(int(usernum))

    #  when number reaches one display the sequence and re-prompt until user quits
    print(sequencelist)
    goagain = input("Would you like to do another number? If yes enter y, otherwise press any key to quit. ")
    if goagain.lower() != "y":
        break
