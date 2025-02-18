
def add_expenses(expenses,amount,category):
    expenses.append({'amount':amount,'category':category })

def print_expenses(expenses):
    for expense in expenses:
        print(f"Amount: {expense['amount']}  Category: {expense['category']}")

def total_expanses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_by_category(expenses, category):
    print_expenses(filter(lambda expense: expense['category'] == category, expenses))
        
def main():
    from colorama import Fore, Style, init
    expenses = [{'amount':25.00,'category':'food'}, {'amount':88.00, 'category':'travel'}]
    while True:
        print(Fore.LIGHTCYAN_EX + "\n21. Add Expenses.")
        print("2. List Expenses.")
        print("3. Show Total Expenses")
        print("4. Filter expenses by category.")
        print("5. Exit")
        choice = input("Enter your choice!: ")
        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            add_expenses(expenses, amount, category)
        elif choice == '2':
            print('\nAll  expenses: ')
            print_expenses(expenses)
        elif choice == '3':
            print(f'\nTotal Expenses :{total_expanses(expenses)}')
        elif choice == '4':
            category = input('Enter Category: ')
            if category in list(map(lambda expense: expense['category'],expenses)):
                print(f'\nExpenses for {category}')
                filter_by_category(expenses, category)
            else:
                print("No Category Found!")   
            
        elif choice == '5':
            break
        else:
            print(Fore.RED + "Please enter a valid choice!\n" + Style.RESET_ALL)

main()