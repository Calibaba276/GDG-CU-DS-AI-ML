def budget_calculator(given_budget):
    total = 0
    while True:
        res = input("Enter expense amount (or 'quit' to stop): ")
        if res == 'quit':
            print("--- Final Summary ---")
            print(f"Total spent: ${total}")
            print(f"Budget remaining: ${round(float(given_budget-total), 2)}")
            break
        else:
            total += round(float(res), 2)
            print(f"Total spent so far: ${total}")
            if total > given_budget:
                print("⚠ Warning: You are over budget!")


if __name__ == "__main__":
    try:
        budget = round(float(input("Enter your total budget: ")), 2)
        budget_calculator(given_budget=budget)
    except ValueError:
        print("Invalid entry!!!")
