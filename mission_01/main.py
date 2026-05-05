total_expense = 0
while True:

    try:
        user_budget = float(input("Enter your budget: "))
        break
    except ValueError:
        print("You can only input a number")

while True:
    user_expense = input("Enter expense amount or quit to stop: ").lower()
   
    if user_expense == "quit":
        print("__Final Summary__")
        print(f"Budget remaining: {user_budget - total_expense}")
        break

    try:
        amount = float(user_expense)
        total_expense += amount
        remaining_budget = user_budget - total_expense
        print(f"Total spent: {total_expense}")
        print(f"Budget remaining: {remaining_budget}")
        
        if total_expense > user_budget:
            print("You are way over your budget!!")
        
    except ValueError:
        print((f"!! Error, You can only input in a number or the word 'quit'. "))

    




    



