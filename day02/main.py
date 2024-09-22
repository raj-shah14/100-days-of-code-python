print("Welcome to the tip calculator!")

bill = float(input("What is the total bill amount?\n$:"))
tip = int(input("How much tip would you like to give?\nPercent:"))
split = int(input("How many people to split the bill?\nPeople:"))

bill_with_tip = bill + (tip * bill)/100
share_for_each_person = bill_with_tip / split

print(f"Each person has to pay {share_for_each_person}")
