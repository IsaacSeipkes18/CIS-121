chances = 0
win = 0
num = 4
while chances < 3 and win != 1:
    user = int(input("guess the number"))

    if user == num:
        print("yay")
        win = 1
    else:
        chances + = 1
