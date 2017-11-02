# Program that converts feet to inches
# November 2, 2017
# CTI-110 M6T2_FeetToInches
# Bethany Reagan

INCHES_PER_FOOT = 12

def main():
    feet = int(input("Enter a number of feet: "))
    print(feet, "feet equals", feetToInches(feet), "inches.")

def feetToInches(feet):
    return feet * INCHES_PER_FOOT

main()
