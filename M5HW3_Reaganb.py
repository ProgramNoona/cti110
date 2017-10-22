# Bethany Reagan
# CSC-133
# October 21, 2017
#
# A program to calculate factorials

#n = int(input("Enter a nonnegative integer: "))

#integer = n

#num = 1

#while n >= 1:
#    num = num * n
#    n = n - 1

#print("The factorial of ", integer, " is ", num)

# Confessions must be made
# I wasn't sure what I was doing, so I looked it up on stackoverflow.com
# Math is hard....

# But then I had a brainwave, and figured it out on my own.
# After several attempts, of course.

integer = int(input("Enter a nonnegative integer: "))

n = integer 
total = 1

for x in range (1, integer):
    total = total * n
    n = n - 1
    

print("The factorial of ", integer, " is ", total)

# And then I scrolled up to the top and realized that this is basically the same
# solution as above, and that I could have done it on my own all along.
# "Believe in yourself", and all that rot.

# Fun fact: the decrement symbol -- (as in --n) does not work in Python.

    





