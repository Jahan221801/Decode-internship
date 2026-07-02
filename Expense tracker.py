sum_expenses = 0

entry = input("Enter an expense (or 'done' to stop): ")

while entry.lower() != "done":
    try:
        amount = float(entry)
        sum_expenses += amount
    except ValueError:
        print("Invalid input. Please enter a number.")

    entry = input("Enter an expense (or 'done' to stop): ")

print("Total Expenses =", sum_expenses)