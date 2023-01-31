# This is a program that allows the user to access two different financial calculators: 
# an investment calculator and a home loan repayment calculator.

import math

print("investment - to calculate the amount of interest you'll earn on your investment \nbond - to calculate the amount you'll have to pay on a home loan \n") 

# The user should be allowed to choose which calculation they want to do.
user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

if user_input == 'investment' or user_input == 'Investment' or user_input == 'INVESTMENT':

    P = float(input('What amount of money you wish to deposit? '))
    interest_rate = float(input('What is the interest rate? Only the number of the interest rate should be entered. '))
    t = float(input('Haw many years you plan on investing? '))
    interest = input('Do you want “simple” or “compound” interest? ')
    r = interest_rate / 100

    if interest == 'simple':
        result = P * (1 + r * t)
        result = round(result, 2)
        print(f'{result} is the total amount once the interest has been applied.')
    elif interest == 'compound':
        result2 = P * math.pow((1 + r), t)
        result2 = round(result2, 2)
        print(f'{result2} is the total amount once the interest has been applied.')
    else:
        print('Please input a valid value. ')
        

elif user_input == 'bond' or user_input == 'Bond' or user_input == 'BOND':

    P = float(input('What is the present value of the house? '))
    interest_rate =  float(input('What is the interest rate? Only the number of the interest rate should be entered. '))
    n = float(input('What is the number of months you plan to take to repay the bond? '))
    i = (interest_rate / 100) / 12
    repayment = (i * P)/(1 - (1 + i)**(-n))
    repayment = round(repayment, 2)
    print(f'The amount that you will have to repay on a home loan each month is {repayment}.') 
    
else:
    print('Please input a valid value.')
   