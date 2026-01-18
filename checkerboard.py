while True:
    w1 = input("Enter the y axis of the square using an integer")
    l1 = input("Enter the x axis of the square using an integer")
    try:
        w1 = int(w1)
        l1 = int(l1)

        white = bool(False)
        black = bool(False)

        if (l1 % 2 != 0 and w1 % 2 == 0) or (l1 % 2 == 0 and w1 % 2 != 0):
            white = bool(True)
        elif (l1 % 2 == 0 and w1 % 2 == 0) or (l1 % 2 != 0 and w1 % 2 != 0):
            black = bool(True)

        if white == bool(True):
            print("That is a white square")
        elif black == bool(True):
            print("That is a black square")
        break
    except ValueError:
        print("Enter an integer dummy")
