# This is a tip calculator program that calculates the total amount each person owes after splitting the bill and adding a tip.
# It takes the bill amount, tip percentage, and number of people as inputs from the user.
# The program then calculates the total amount including the tip and divides it by the number of people to find out how much each person owes.

myBill = float(input("What was the bill amoount?\n: "))
tip= int(input("\nHow much % of tip would you like to give? 10, 15, or 20?\n: "))
totalamount= myBill * (1 + tip/100)
numberOfPeople = int(input("How many people?: "))
answer = totalamount / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)