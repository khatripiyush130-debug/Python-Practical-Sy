# Monthly Expense Tracker

print("===== Monthly Expense Tracker =====")

# Input number of days
days = int(input("Enter the number of days: "))

total_expense = 0

# For loop for each day
for day in range(1, days + 1):
    print("\nDay", day)

    # Input number of expenses for the day
    n = int(input("Enter number of expenses: "))

    count = 1
    day_total = 0

    # While loop to enter expenses
    while count <= n:
        expense = float(input("Enter expense " + str(count) + ": "))
        day_total = day_total + expense
        count = count + 1

    print("Total expense for Day", day, "=", day_total)

    # Accumulation
    total_expense = total_expense + day_total

print("\n===== Monthly Expense Summary =====")
print("Total Monthly Expense =", total_expense)