shouldCalculate = True
total = 0.00
taxPaid = 0.00
subTotal = 0.00
salesTax = .075
budget = input("What is your budget? $")
budget = float(budget)
amountOfMoneyLeft = 0.00
amountOfMoneyBeforeTax = 0.00

def calculateMoneyBeforeTax(amountLeft):
    global salesTax
    findMoneyLeft = 100 + (salesTax * 100)
    beforeTax = amountLeft / (findMoneyLeft/100)
    return beforeTax

def output(total, subTotal, taxPaid, amountOfMoneyLeft, amountOfMoneyBeforeTax):
    total = round(total, 2)
    subTotal = round(subTotal, 2)
    taxPaid = round(taxPaid, 2)
    amountOfMoneyLeft = round(amountOfMoneyLeft, 2)
    amountOfMoneyBeforeTax = round(amountOfMoneyBeforeTax, 2)
    
    print("\nYour subtotal is at $" + str(subTotal) + " which is a total of $" + str(total) + " after paying $" + str(taxPaid) + " in taxes.")
    if (amountOfMoneyLeft > 0):
        print("You have $" + str(amountOfMoneyLeft) + " left in your budget. ($" + str(amountOfMoneyBeforeTax) + " before taxes.)\n")
    else:
        print("I mean.... you can keep going, but you're out of money!\n")

def calculate(number):
    global shouldCalculate
    global total
    global taxPaid
    global subTotal
    global salesTax
    global budget
    global amountOfMoneyLeft
    global amountOfMoneyBeforeTax

    try:
        number = float(number)
        subTotal += number
        taxPaid = subTotal * salesTax
        total = subTotal + taxPaid
        amountOfMoneyLeft = budget - total
        amountOfMoneyBeforeTax = calculateMoneyBeforeTax(amountOfMoneyLeft)
        output(total, subTotal, taxPaid, amountOfMoneyLeft, amountOfMoneyBeforeTax)
    except ValueError:
        print("Something went horribly wrong.")
        shouldCalculate = False

while (shouldCalculate):
    number = input("Enter the price of an item: $")
    calculate(number)
