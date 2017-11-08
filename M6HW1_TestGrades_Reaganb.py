# This program accepts, averages, and assigns letters to grades.
# November 7, 2017
# CTI-110 M6HW1 - Test Average and Grade
# Bethany Reagan
#

def main():
        
    g1 = float(input("Please enter a grade: "))
    g2 = float(input("Please enter another grade: "))
    g3 = float(input("Please enter another grade: "))
    g4 = float(input("Please enter another grade: "))
    g5 = float(input("Okay, last one: "))

    average = calc_average(g1, g2, g3, g4, g5)

    print("\nThe average of these grades is ", average, "\n")

    l1 = determine_grade(g1)
    l2 = determine_grade(g2)
    l3 = determine_grade(g3)
    l4 = determine_grade(g4)
    l5 = determine_grade(g5)

    print("The first student gets: ", l1)
    print("The second student gets: ", l2)
    print("The third student gets: ", l3)
    print("The fourth student gets: ", l4)
    print("The fifth student gets: ", l5)


def calc_average(a, b, c, d, e):
    total = a + b + c + d + e
    return total / 5


def determine_grade(vari):
    if vari > 89:
        return "A"
    elif vari > 79:
        return "B"
    elif vari > 69:
        return "C"
    elif vari > 59:
        return "D"
    else:
        return "F"
    
    







main()
