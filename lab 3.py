"""
Isaac Seipke
98/9/22

Description of what this program does
"""
from re import M
import sys

zero = 0
taxOwed = 0.0

earnedIncome = float(input("Enter the amount of income you earned in 2021: "))
if earnedIncome < 0:
	print("You made less than $0. Contact an accountant")
	sys.exit()

print("Are you married or single?")
maritalStatus = input("Type m for married and s for single: ")


#Ensures you have a valid marital status
while maritalStatus != "m" and maritalStatus != "s":
	print("you entered an invalid marital status")
	maritalStatus = input("Type m for married and s for single: ")




# Your code goes here

if maritalStatus == "s": #This checks to see if they user is single
	print("Sorry you will find someone") 
	if earnedIncome <= 0: 
		print("Sorry get a job")
	if earnedIncome > 0 and earnedIncome < 9951:
		print("you owe", earnedIncome * .10,"in taxes.") #This calculates to see if youn make enough income for the first bracket and tells you how much you owe
	elif earnedIncome > 9950 and earnedIncome < 40526:
		print("you owe", ((earnedIncome - 9950) * .12) + 995,"in taxes.") #This subtracts $995 because it detected that you are in the second bracket
	elif earnedIncome > 40525 and earnedIncome < 86376:
		print("you owe",((earnedIncome - 9950 - 40525) * .22) + 995 + 4863 ,"in taxes.")
	elif earnedIncome > 86375: #This checks to see if you make more money than the calculator can calculate
		print("Wow you make a lot of money, Can I have some?")
if maritalStatus == "m":
	print("congratulations") 
	if earnedIncome <= 0: #This is checking to see if you make less than or equal to zero
		print("Sorry get a job")
	if earnedIncome > 0 and earnedIncome < 19901:
		print("you owe", earnedIncome * .10,"in taxes.")
	elif earnedIncome > 19900 and earnedIncome < 81051:
		print("you owe", ((earnedIncome - 19900) * .12) + 1990,"in taxes.")
	elif earnedIncome > 81050 and earnedIncome < 172751: print("you owe",((earnedIncome - (81050 + 19900)) * .22) + ((81050)*.12) + (19900*.10),"in taxes.") #This formula does everything from above but for the final bracket
	elif earnedIncome > 172750:
		print("Wow you make a lot of money, Can I have some?") 
#((((((earnedIncome-19900-81050)*.22))))+1990)
	