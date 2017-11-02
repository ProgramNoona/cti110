# Bethany Reagan
# CTI-110
# November 2, 2017
#
# This program converts kilometers to miles

CONVERSION_FACTOR = 0.6214

def main():
    #Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    #Display the distance converted to miles
    showMiles(kilometers)

    input("Go America!")

def showMiles(km):
    # Calculate miles.
    miles = km * CONVERSION_FACTOR

    # Display the miles.
    print(km, 'kilometers equals', miles, 'miles.\n')

main()
