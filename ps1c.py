# House Hunting program v.3, tells you how much money you need
# to save per month to afford a $1M house in 36 months
# Use bisection search, can be within $100 dollars of the $1M

# variable of interest is now portion_saved
#--------------------------------------------

# User inputs
original_annual_salary = float(input("Enter your annual salary: "))


# declare main variables
total_cost = 1000000
portion_down_payment = 0.25
current_savings = 0
months = 36
r = 0.04
semi_annual_raise = .07

# declare variables for bisection search
epsilon = 100
num_guesses = 0
low = 0
high = 1
portion_saved = 1
total_portion = total_cost*portion_down_payment
#print("portion saved",portion_saved)

# Loop that keeps track of search success
while abs(current_savings - total_portion) >= epsilon:
    # loop that does 36 month guess calculation
    # Returns current_savings, get closer $1M * 0.25
    current_savings = 0
    months = 0
    annual_salary = original_annual_salary
    while months < 36:
        current_savings += current_savings*r/12
        current_savings += portion_saved*annual_salary/12
        #print('current savings in loop', current_savings)
        if months > 1 and months % 6 == 0:
            annual_salary += annual_salary*semi_annual_raise
        months += 1

    # first test case, checks if salary is high enough to use
    if portion_saved == 1 and current_savings - total_portion < epsilon:
        print("It is not possible to pay the down payment in three years.")
        break

    # print('current_savings: ',current_savings)
    # bisection search is looking for the savings rate,
    # that multiplies the salary
    if current_savings < total_portion:
        # too low, look in upper half of search
        low = portion_saved
    else:
        # too high, look in lower half of search
        high = portion_saved

    portion_saved = (high + low)/2
    #print('portion_saved: ',portion_saved)
    num_guesses += 1
    #print('number of guesses',num_guesses,'\n')
    if num_guesses > 100:
        break

# Print if salary large enough to afford
if portion_saved != 1:
    print('Best savings rate: {:0.4f}'.format(portion_saved))
    print('Steps in bisection search:', num_guesses)
