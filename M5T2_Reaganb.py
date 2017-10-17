#Bethany Reagan
#CTI 110
#October 12, 2017
#Program to accept and display the number of bugs collected in seven days.

print('Dearest Maureen, would you collect some insects for my collection, please?')
answer = input("y or n?: ")

if answer == 'y':
   print("Why, thank you, dear!\n")
else:
   print("Do it anyway.\n")

total = 0

for day in range (1, 8):
    print('Enter the bugs collected on day', day)
    bugs =int(input())
    total += bugs

print('You collected a total of', total, 'bugs.\n')

pathetic = 10
okay = 20
nice = 30
great = 40

if total >= great:
    print("Magnificent!  We shall have the good cakes for tea-time today!")
elif total >= nice:
    print("You have done very nicely, dear!  Come and wash your hands.")
elif total >= okay:
    print("You have done well enough.  Come to tea.")
elif total >= pathetic:
    print("How disappointing.  Well, I suppose you did your best.")
else:
    print("Pathetic.  I suppose you couldn't be bothered to even dirty your hands.")

input("Come along now.")




