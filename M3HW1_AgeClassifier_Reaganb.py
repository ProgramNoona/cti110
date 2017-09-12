# CTI-110
# M3HW1 - Age Classifier
# Bethany Reagan 
# September 12, 2017
#
# A program to classify someone by their age.

def main():
    adult = 20
    teen = 13
    baby = 1
    
    age = int(input("Please tell me your age, Maureen. "))

    if age >= adult:
        print("You've blossomed into a lovely adult.  Shall we have a smoke?\n")
    elif age >= teen:
        print("Dear, you are but a teenager.  You do not know everything.\n")
    elif age > baby:
        print("Would you like a cookie, dear child?\n")
    else:
        print("My!  What an intelligent infant to use a computer!\n")

    input("Please press enter and come to tea.")








main() 
