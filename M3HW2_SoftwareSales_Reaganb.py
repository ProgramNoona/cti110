# CTI-110
# M3HW2 - Software Sales
# Bethany Reagan
# September 12, 2017
#
# A program wherein sales and possible discounts are calculated, and tiny
# digital people are appreciated.

def main():
    print("Greetings, enlightened customer!  Welcome to Luxury Computer Care!")
    print("We here at LCC promote only the best in fine luxury software for \
the little people living inside your computer.  After all, how would our \
computers run without our dear digital citizens processing all those ones \
and zeroes?")
    print("We are offering a special package today for only $99!  If you buy \
this package and download it to your computer, you will install a digital \
cafeteria, restaurant, bowling alley, bank, post office, hospital or other \
wonderful place of patronage for your dear computer people!")
    
    unitsSold = int(input("How many would you like to buy? "))

    unitCost = 99
    
    if unitsSold > 99:
        discount = .4
        print("You get the forty percent discount!\n")
    elif unitsSold > 49:
        discount = .3
        print("You get the thirty percent discount!\n")
    elif unitsSold > 19:
        discount = .2
        print("You get the twenty percent discount!\n")
    elif unitsSold > 9:
        discount = .1
        print("You get the ten percent discount!\n")
    else:
        print("\n")
        discount = 0
        saved = 0

    gross = unitCost * unitsSold
    if discount != 0:
        saved = discount * gross
    total = gross - saved    

    print("You have chosen to buy ", unitsSold, " packages!")
    print("Your total is $", total)
    print("You saved $", saved, " dollars.\n")

    input("Thanks for shopping at Luxury Computer Care!")
    
    
    





main()
