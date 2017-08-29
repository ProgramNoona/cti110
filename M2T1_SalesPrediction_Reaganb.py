# CTI-110 
# M2T1 - Sales Prediction
# Bethany Reagan
# August 29, 2017
#
# A program for calculating projected yearly profit.

# Get projected sales
total_sales = float(input('Enter the projected sales: '))

# Calculate profit
annual_profit = total_sales * 0.23

# Prints calculated profit to screen
print('The profit is ', '$', format(annual_profit, ',.2f'))
