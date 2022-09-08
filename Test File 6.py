#Create a script that asks the user for their income. If the income is greater than 450000 say "Damn you rich", if they make less say "you got it"
income = float(input("How much do you make?"))

if income > 450000:
    print("Damn you rich")
elif income < 450000:
    print("You got it")