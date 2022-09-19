#Boolean
#winner = True
#loser = False
x = int(input("Enter number here: "))
if 35 <= x <= 1000:
    if x >= 100:
        print(100)
    else:
        while x <=100:
            if x % 2 == 0:
                print(x)
            x += 1
else:
    print("You did not enter a valid number :")