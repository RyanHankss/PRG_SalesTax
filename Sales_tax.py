#use 7.2 update variables to initalize
price = 1
totalPrice = 0

#instructions

print('Input the cost of each individual item, after you have entered all items type 0.\n')

while price != 0:
    strPrice = raw_input("Enter the amount of an item: \n")

    price = float(strPrice)

    totalPrice += price

else:
    print('Your total before tax is $' + str(totalPrice) + '\n')


print('Tax is 6% and will be added to your total.\n')

taxTotal = totalPrice * 0.06

strTax = str(taxTotal)

print('The total tax on your items is $' + strTax + '\n')

completeTotal = totalPrice + taxTotal

strTotal = str(completeTotal)

print('Your bill comes to the amount of $' + strTotal)
