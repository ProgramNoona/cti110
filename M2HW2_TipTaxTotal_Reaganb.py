# CTI-110
# M2HW2 - Tip Tax Total
# Bethany Reagan
# August 31, 2017
#
# Program to calculate cost of meal + tips.

mealCost = float(input("How much did your meal cost? "))

print("\n")

taxPercent = .07
tipPercent = .18

tax = taxPercent * mealCost
print("The tax for the meal is", tax)

tip = tipPercent * mealCost
print("The tip for the meal is", tip)

totalCost = mealCost + tax + tip
print("The total cost for your meal is", totalCost, "\n\n")

input("Press ENTER to exit the program.")


