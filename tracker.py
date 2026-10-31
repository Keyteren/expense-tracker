# Project: Expense Tracker - Installment 4
# Author: Katherine C. Salvacion
# Description: Tracker takes input, applies tax, checks budget, and makes decisions

# Top banner
print("=" * 40)

# Title and tagline
print("\t    EXPENSE TRACKER")
print("\tKnow where your money goes.")

# Bottom banner
print("=" * 40)

# Main menu
print()
print("MAIN MENU")
print("\t[1] Add an expense\t(coming soon)")
print("\t[2] View all expenses\t(coming soon)")
print("\t[3] Show total spent\t(coming soon)")
print("\t[4] Exit\t\t(coming soon)")
print()

# Ask for the user's name
name = input("What's your name? ")

# Personal greeting
print("Welcome,", name + "!", "Let's log two expenses.")

# Start subtotal at 0
subtotal = 0

# Ask for first expense and update subtotal
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal = subtotal + amount1

# Check size of first expense
if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

# Ask for second expense and update subtotal
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal = subtotal + amount2

# Check size of second expense
if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

# Check if both expenses are over 100
if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

# Compute average from subtotal
average = subtotal / 2

# Ask for tax rate (whole number)
tax_percent = int(input("Tax rate %? "))

# Compute tax and grand total
tax = subtotal * tax_percent / 100
grand_total = subtotal + tax

# Ask for budget
budget = float(input("Your budget? "))

# Check if over budget
over_budget = grand_total > budget

# Calculate amount left in budget
left = budget - grand_total

# Summary
print()
print("-" * 40)
print("SUMMARY")
print("\t-", item1 + ":\t$" + str(amount1))
print("\t-", item2 + ":\t$" + str(amount2))
print("\tSubtotal:\t$" + str(subtotal))
print("\tAverage:\t$" + str(average))
print("\tTax", "(" + str(tax_percent) + ".0%):\t$" + str(tax))
print("\tGrand total:\t$" + str(grand_total))

# Give one budget verdict
if over_budget:
    print("Over budget by $" + str(grand_total - budget) + "!")
elif grand_total > budget * 0.90:
    print("Careful: only $" + str(left) + " left.")
else:
    print("Within budget. $" + str(left) + " left.")

print("-" * 40)

# Footer
print("Made by: Katherine C. Salvacion | Installment 4")