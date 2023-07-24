print("Welcome to the tip calculator!")

bill = float(input("What is the total bill amount?\n$ "))
tip = int(input("How much tip would you like to give?\nPercent "))
split = int(input("How many people to split the bill?\nPeople "))

tips = (tip/100)
to = bill * tips
total = (bill  + to)/ split
totals = ('{:.02f}'.format(total))

print(f"Each person should pay: ${totals}")