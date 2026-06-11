# revision(print, variables, int(), input) and string foramting

print("---Age Calculator---")

current_year = 2026 

birth_year = int(input('What is your birth year? ')) 

age = current_year - birth_year 

x = 197972


# f-string 

print(f"You are {age} and your birth year is {birth_year} and the current year is {current_year} and x is {x}")


# str.format()

print("You are {} and your birth year is {} and the current year is {}".format(age, birth_year, current_year)) #sequential placeholders


print("You are {1} and your birth year is {0} and the current year is {2}".format( birth_year, age, current_year)) #positional indexing



print("You are {user_age} and your birth year is {user_birth_year} and the current year is {the_current_year}".format(user_age = age, 
user_birth_year = birth_year, the_current_year = current_year)) #keyword argument




# You are age and your birth year is birth_year and the current year is current_year