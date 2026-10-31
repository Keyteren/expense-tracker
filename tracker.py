
# Project: Expense Tracker - Installment 5
# Author: Katherine C. Salvacion
# Description: Tracker uses a menu to add expenses, view totals, and check budget

# Top banner
print("=" * 40)

# Title and tagline
print("\t    EXPENSE TRACKER")
print("\tKnow where your money goes.")

# Bottom banner
print("=" * 40)

# Ask for setup information
name = input("What's your name? ")
tax_percent = int(input("Tax rate %? "))
budget = float(input("Your budget? "))

# Welcome message
print("Welcome,", name + "!")

# Initialize expense tracking variables
subtotal = 0
count = 0

# Main menu loop
while True:
    print()
    print("MAIN MENU")
    print("\t[1] Add an expense")
    print("\t[2] View all expenses (coming soon)")
    print("\t[3] Show total spent")
    print("\t[4] Exit")

    choice = input("Choose 1-4: ")

    # Option 1: Add an expense
    if choice == "1":
        amount = float(input("Amount? "))

        # Update subtotal and count
        subtotal = subtotal + amount
        count = count + 1

        # Check expense size
        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")

    # Option 2: View all expenses
    elif choice == "2":
        print("Coming soon: the tracker can't remember each item yet.")

    # Option 3: Show total spent
    elif choice == "3":
        tax = subtotal * tax_percent / 100
        grand_total = subtotal + tax

        # Display expense summary
        print()
        print(f"{'Expenses:':<16}{count}")
        print(f"{'Subtotal:':<16}${subtotal:.1f}")
        print(f"{f'Tax ({tax_percent:.1f}%):':<16}${tax:.1f}")
        print(f"{'Grand total:':<16}${grand_total:.1f}")

        # Check budget
        over_budget = grand_total > budget

        if over_budget:
            print(f"Over budget by ${grand_total - budget:.1f}!")
        elif grand_total > budget * 0.9:
            print(f"Careful: only ${budget - grand_total:.1f} left.")
        else:
            print(f"Within budget. ${budget - grand_total:.1f} left.")

    # Option 4: Exit
    elif choice == "4":
        print("Goodbye,", name + "!")
        print("-" * 40)
        print("Made by: Katherine C. Salvacion | Installment 5")
        print("=" * 40)
        break

    # Invalid choice
    else:
        print("Please choose 1, 2, 3 or 4.")
