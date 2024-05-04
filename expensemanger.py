class ExpenseManager:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def display_expenses(self):
        print("\nExpense Summary:")
        for category, amount in self.expenses.items():
            print(f"{category}: {amount}")


def main():
    manager = ExpenseManager()

    while True:
        print("\nExpense Manager")
        print("1. Add Expense")
        print("2. Display Expenses")
        print("3. Quit")

        choice = input("Enter your choice: ")

        try:
            choice = int(choice)

            if choice == 1:
                category = input("Enter expense category: ")
                amount = float(input("Enter expense amount: "))
                manager.add_expense(category, amount)
                print("Expense added successfully!")
            elif choice == 2:
                manager.display_expenses()
            elif choice == 3:
                print("Exiting the expense manager.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nExpense manager interrupted. Exiting...")
            break
        except Exception as e:
            print("An error occurred:", e)


if __name__ == "__main__":
    main()
