class expensetracker:
    def __init__(self):
        self.transaction ={
            "expense" :[]
        ,
        "income" :[],
        }
        

    def storeTransaction(self,type,category,cost,desc,date):
            transaction ={
                "category":category,
                "cost":cost,
                "Description": desc,
                "date": date,
            }
            if type == "expense":
                self.transaction["expense"].append(transaction)
            else:
                self.transaction["income"].append(transaction)   


            return True
    def view_transaction(self):
        print("Income")
        for expense in self.transaction['expense']:
            print(expense)

            print("EXpenses")
            for expense in self.transaction ["expense"]:
                print(expense)

    def total_incomeexpense(self):
        print("Total Income")
        total_income = 0
        for income in self.transaction['income']:
            print(income["cost"])
        
        print("total Expense")
        total_expense = 0
        for expenses in self.transaction["expense"]:
            total_expense += expenses["cost"]
        print(total_expense)

mytransaction = expensetracker()  
mytransaction.storeTransaction("expense","Electricity Bill",4500,"MDHC","20/10/23")
mytransaction.storeTransaction("expense","Pocket Money",1500,"nill","20/10/23")
mytransaction.storeTransaction("expense","Grocery",2000,"homeC","20/10/23")

mytransaction.view_transaction()
mytransaction.total_incomeexpense()




        
