# CTI-110
# M3T1 - Areas of Rectangle
# Bethany Reagan
# September 11, 2017
#
# Program to calculate the area of two rectangles and compare areas.

print("This program will calculate the area of two rectangles.\n");
print("What are the dimensions of the first rectangle?");

width1 = int(input("Enter the width: "));
height1 = int(input("Enter the height: "));

area1 = width1 * height1;

print("\nOkay, now for the second rectangle.");

width2 = int(input("Enter the width: "));
height2 = int(input("Enter the height: "));

area2 = width2 * height2;

if area1 > area2:
       print("\nRectangle 1 is larger than rectangle 2.");
elif area2 > area1:
       print("\nRectangle 2 is larger than rectangle 1.");
else:
        print("\nBoth rectangles have the same area.");
