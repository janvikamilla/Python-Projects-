print("===== EXPENSE SPLITTER =====")

total_bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))

if total_bill >= 0 and people > 0:
    share = total_bill / people

    print("\nTotal Bill:", total_bill)
    print("Number of People:", people)
    print("Each Person Pays: ₹", round(share, 2))

else:
    print("Invalid input!")

print("\nThank you for using Expense Splitter!")
