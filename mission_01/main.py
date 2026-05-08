budget = "hi this is muna building a budget tracker, toodles"
print(budget) 

budget = float(input("Enter your total budget: "))

total_spent = 0

while True:
    expense = input("Enter expense amount (or 'quit' to stop): ")

    
    if expense.lower() == "quit":
        break

    
    expense = float(expense)
    total_spent += expense

    
    print(f"Total spent so far: ${total_spent:.2f}")

    
    if total_spent > budget:
        print(" Warning: You are over budget")

# Calculate remaining budget
remaining_budget = budget - total_spent

# Final summary

print(f"\nTotal spent: ${total_spent:.2f}")
print(f"Budget remaining: ${remaining_budget:.2f}")