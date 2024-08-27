print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip you would like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

#Calculate how much each person should pay
total_bill = bill + tip / 100 * bill
each_has_to_pay = total_bill / people
print('Each has to pay: $',round(each_has_to_pay,2))