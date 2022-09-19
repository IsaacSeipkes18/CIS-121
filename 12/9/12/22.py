#Write a small script that asks the user for a number between 35-1000.
#When the user enters the number your program should print the numbers from that x number to 100
#but if the number goes over 100 just print 100 by itself

from multiprocessing.resource_sharer import stop


number = int(input("Pick a number 35-1000: "))

while number <= 100 and number >= 35:
    if number/2 % 1:
        number + 1
    else:
        print(number)
    number += 1
if number > 101 and number < 1000:
    print("100")
if number < 35 or number > 1000:
    print("Invalid Number")
    