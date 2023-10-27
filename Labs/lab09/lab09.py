import csv  # Import the CSV module

class ExpenseTracker:
    def __init__(self):
        self.transactions = []  # Initialize an empty list to store transactions

    def storeTransaction(self, transaction_type, category, cost, desc, date):
        # Store a new transaction as a dictionary
        new_transaction = {
            "Type": transaction_type,
            "Category": category,
            "Cost": cost,
            "Description": desc,
            "Date": date,
        }
        self.transactions.append(new_transaction)  # Append the transaction to the list
        return True

    def view_transaction(self):
        print("Transactions:")
        for transaction in self.transactions:
            print(transaction)  # Print each transaction

    def total_incomeexpense(self):
        # Calculate total income and total expense separately
        total_income = sum(transaction["Cost"] for transaction in self.transactions if transaction["Type"] == "Income")
        total_expense = sum(transaction["Cost"] for transaction in self.transactions if transaction["Type"] == "Expense")

        print("Total Income:", total_income)
        print("Total Expense:", total_expense)

    def show_menu(self):
        while True:
            print('\n...MY EXPENSE TRACKER MENU...')
            print('1. Add Income')
            print('2. Add Expense')
            print('3. View Transactions')
            print('4. Total Income and Expense')
            print('5. Exit')

            choice = int(input('Enter your choice: '))  # Get user's choice as an integer

            if choice == 1:
                print('Enter the details of income')
                category, cost, desc, date = self.get_input()
                self.storeTransaction('Income', category, cost, desc, date)  # Store income transaction
            elif choice == 2:
                print('Enter the details of expense')
                category, cost, desc, date = self.get_input()
                self.storeTransaction('Expense', category, cost, desc, date)  # Store expense transaction
            elif choice == 3:
                self.view_transaction()  # View transactions
            elif choice == 4:
                self.total_incomeexpense()  # Display total income and expense
            elif choice == 5:
                break  # Exit the loop and end the program
            else:
                print('Invalid choice')

    def get_input(self):
        category = input('Enter Category: ')
        cost = int(input('Enter the amount: '))
        desc = input('Enter description: ')
        date = input('Enter Date (DD-MM-YYYY): ')
        return category, cost, desc, date  # Return input values

    def export_to_file(self, filename):
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            for transaction in self.transactions:
                if transaction != self.transactions[0]:
                    writer.writerow([
                        transaction["Type"],
                        transaction["Category"],
                        transaction["Cost"],
                        transaction["Description"],
                        transaction["Date"]
                    ])
        print('Transactions appended to the file.')

def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        for values in reader:
            if len(values) == 5:
                transaction_type, category, cost, desc, date = values
                my_transaction.storeTransaction(transaction_type, category, int(cost), desc, date)  # Store transactions from CSV

        return True


my_transaction = ExpenseTracker()  # Create an instance of ExpenseTracker

# Read transactions from the CSV file
read_csv("D:\Python\git\MscDSA-MDA171-23122037\lab09\python lab09.csv")

# Display the menu to the user
my_transaction.show_menu()  # Display the menu and handle user interactions
my_transaction.export_to_file("D:\Python\git\MscDSA-MDA171-23122037\lab09\python lab09.csv")  # Export transactions to the CSV file