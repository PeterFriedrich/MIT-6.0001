# House Hunting program, tells you how many months it takes
# till you can afford a down payment for a house

# User inputs
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save,\
as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

# declare additional variables
portion_down_payment = 0.25
current_savings = 0
months = 0
r = 0.04

# loop that terminates when enough money has been made
while True:

    if current_savings >= total_cost * portion_down_payment:
        print("Number of months:", months)
        break

    else:
        current_savings += current_savings*r/12
        current_savings += portion_saved*annual_salary/12
    months += 1
