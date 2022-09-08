#Create a guessing game. Give the user 3 chances. If they get it right print("yay"). If not make a custom message

number = int(input("Pick a number 1-5"))
tries = 2
if number == 2:
    print("sorry try again")
if number == 3:
    print("sorry try again")
if number == 4:
    print("sorry try again")
if number == 5:
    print("sorry try again")
while number == 1:
    number = number + 1
    print("yay")
