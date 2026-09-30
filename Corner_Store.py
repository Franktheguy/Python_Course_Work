# Corner Store Program
# Purpose: Keep track of daily sales

cashDrawer = 100.00
productID = 0
quantity = 0
price = 0.0
subtotal = 0.0
salesTax = 0.0
totalSale = 0.0
taxRate = 0.0
anotherSale = 'y'

print()
print("----------[ C o r n e r   S t o r e ]----------")
print()

# Loop for each sale 
while anotherSale.lower() == 'y':
    
    # Enter the first productID
    print()
    productID = input('Enter the first Product ID (-1 to end): ')
    productID = int(productID)

    # Loop for each product
    while productID != -1:

        # Enter the quantity
        quantity = input("Enter the quantity: ")
        quantity = int(quantity)

        

        # Look up price and whether it is taxable
        if productID == 101:
            price = 3.95
            taxRate = 0.0
        elif productID == 102:
            price = 1.85
            taxRate = 0.075
        elif productID == 103:
            price = 2.49
            taxRate = 0.075
        elif productID == 104:
            price = 5.19
            taxRate = 0.075
        elif productID == 105:
            price = 4.99
            taxRate = 0.0


        else:
            print("Error: product ID not found!")


        
        # Add to subtotal and salesTax
        subtotal += price * quantity
        salesTax += price * quantity * taxRate

        
        # Get next productID
        productID = input('Enter the next Product ID (-1 to end): ')
        productID = int(productID)

    # End of while loop

    # Add subtotal and salesTax to totalSale
    totalSale = subtotal + salesTax

    
    # Print out receipt
    print()
    print(f"Subtotal:  ${subtotal: 7.2f}")
    print(f"salesTax:  ${salesTax: 7.2f}")
    print(f"totalSale: ${totalSale: 7.2f}")
    print()

    # Add Total Sale to Cash Drawer
    cashDrawer += totalSale

    # Zero out subtotal and salesTax
    subtotal = 0.0
    salesTax = 0.0
    
    # Ask for another sale
    anotherSale = input("Would you like another sale ('y' or 'n')? ")

# Print out cash drawer
print()
print(f"Total in cash drawer: ${cashDrawer: 7.2f}")

            

