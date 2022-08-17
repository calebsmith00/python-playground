total = 0
count = 0
def calculate(number):
    global count
    global total
    total += number
    count += 1

shouldCalculate = True

def totalOutput():
    print("Sweet! That's a total of " + str(total) + " with " + str(count) + " total transactions.")
    try:
        average = float(total / count)
        print("Among those numbers, it seems like " + str(average) + " was the average.")
    except ValueError:
        print("Error casting to double.")

while (shouldCalculate):
    number = input("Enter a number to add: \n")
    try:
        number = float(number)
        calculate(number)
    except ValueError:
        shouldCalculate = False

totalOutput()
        
