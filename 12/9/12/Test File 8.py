#Create a script that asks the user for their name income. Lets the user know how much money they would haveif they didnt spend any money in 20 years
name = input("Enter name: ")
money = int(input("How much do you make in a year: "))
years = 1
income = 0
print("Hey", name, "you make", money, "a year!")
print("This is how much you would have in 20 years")
while income < 10000 and years != 10000000000000:
    income = money * years
    print("$"+str(income), "Year", years)
    years += 1

    
    #Let the user know how many years it will take to get 10k