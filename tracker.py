# Project: Expense Tracker - Installment 3
# Author: Katherine C. Salvacion
# Description: Tracker takes input, applies tax, checks budget

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

# Ask for first expense and update subtotal right after
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal = subtotal + amount1

# Ask for second expense and update subtotal right after
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal = subtotal + amount2

# Compute average from subtotal
average = subtotal / 2

# Ask for tax rate (whole number)
tax_percent = int(input("Tax rate %? "))

# Compute tax and grand total
tax = subtotal * tax_percent / 100
grand_total = subtotal + tax

# Ask for budget
budget = float(input("Your budget? "))

# Over budget? True / False
over_budget = grand_total > budget

# Left in budget 
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
print("\tOver budget?:\t" + str(over_budget))
print("\tLeft in budget:\t$" + str(left))
print("-" * 40)

# Footer
print("Made by: Katherine C. Salvacion | Installment 3")