#Write a scrpit that keeps asking the user for a nummber and check if the number is even or odd. Let the user know what it is. 
#If they enter the number 0 stop asking for numbers

done = False

while done != True:
    number = int(input("Please enter a number: "))
    if number == 0:
        print("Bye!")
        done = True
    elif number % 2 == 0:
        print("This is a even number")
    else:
        print("This is an odd number")

