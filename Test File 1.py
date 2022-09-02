#asking user for age/converting input str to int
human_age = float(input("How old are you?"))
dog_year = 7
basic_years = float(human_age*dog_year)
basic_years2 = int(human_age*dog_year)
months = basic_years - basic_years2
months2 = float(12*months)
months3 = int(12*months)
months4 = months2 - months3
days2 = int(31*months4)
print("If you are",human_age,"years old","you would be",(basic_years2),"years",months3,"months",days2,"days","old in dog years.")