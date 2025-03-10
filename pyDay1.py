''' 
print("Vanakkam")
name = input("Enter your name: ")
print(len(name))
'''
'''
#Band_name_generator
print("Welcome to the Band Name Generator.")
city_name = input("What's the name of the city you grew up in?\n")
pet_name = input("What's your pet's name?\n")
band_name = city_name +" "+pet_name
print("Your band name could be " + band_name)
'''
'''
print(type(1))
print(type("a"))
print(type(0.1))
print(type(True))
'''
'''
#tip calculator
print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
ppl = int(input("How many people to split the bill?"))
final_amount = (total *(tip / 100) + total) / ppl
rounded_result = round(final_amount,2)
print(f"Each person should pay: ${rounded_result}")
'''
'''
#assignment_1

name = "Anand"
balance = 15
year = 2025

print(f"""
Dear {name},
You have {balance} days of leave balance for this
year {year}.""")
'''

#assignment_2

name = input("Enter your name: ")
email = input("Enter your Email Id: ")
phone = input("Enter your Phone number: ")

print(f"""
User_Name : {name}
Email_ID : {email}
Ph : {phone}""")