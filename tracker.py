# Project: Expense Tracker - Installment 2
# Author: Katherine C. Salvacion
# Description: Tracker takes input

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

# Ask for two expenses 
item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

# Compute total and average 
total = amount1 + amount2
average = total / 2

# Summary 
print()
print("-" * 40)
print("SUMMARY")
print("  -", item1 + ":\t\t$" + str(amount1))
print("  -", item2 + ":\t\t$" + str(amount2))
print("Total spent:\t\t$" + str(total))
print("Average:\t\t$" + str(average))
print("-" * 40)

# Footer
print("Made by:", name, " | Installment 2")