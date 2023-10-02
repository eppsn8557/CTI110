# This program calculates and displays travel expenses
# 1 October 2023
# CTI-110 P1HW2-Travel Expense
# Nadia Epps
#
print('This program calculates and displays travel expenses')
budget = int(input('Enter Budget:'))
print('Enter your travel destination:', end=' ')
location = input()
fuel = int(input('How much do you think you will spend on gas?'))
acc = int(input('Approximately, how much will you need for accomodation/hotel?'))
food = int(input('Last, how much do you need for food?'))
print('------------Travel Expenses------------')
print('Location:', location)
print('Initial Budget:', budget)
print(end='\n')
print('Fuel:', fuel)
print('Accomodation:', acc)
print('Food:', food)
print(end='\n')
print(budget - fuel - acc - food)



ploading P1HW2_EppsNadia.py…]()
