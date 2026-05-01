"""A Smart Budget and Expense Tracker Tool."""

# Prompt user for their monthly budget
budget = float(input("Enter your monthly budget: "))

# Initialize total expenses
total_expenses = 0.0

# Loop to get expenses from the user
while True:
    # Prompt user for an expense or to quit
    expense = input(
        "\nTo exit enter 'quit'"
        "\nEnter your expense: ")
    
    # Condition to end program
    if expense.lower().strip() == 'quit':
        break
    
    # To handle wrong inputs like letters or other unexpected inputs
    try:
        total_expenses += float(expense) # Expense gets added to total expense
        print(f"Total expenses so far: {total_expenses:.2f}")
    except ValueError:
        print("Please enter a valid number for the expense.")

    if total_expenses > budget:
        print("Warning: You have exceeded your budget!")

# Print out total expenses and remaining budget
print(f"\nTotal expenses: {total_expenses:.2f}")
print(f"Remaining budget: {budget - total_expenses:.2f}")