#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("welcome to your new tip calculator!")

bill = float(input("what is the total value of your bill? £"))
tip = int(input("what percentage of a tip would you like to give? 10, 12 or 14?"))
guests = int(input("How many guests are in your party?" ))

bill_tot = tip/100*bill + bill

share = (round(bill_tot/guests, 2))

print(f"Each person has to pay - £{share}.")
