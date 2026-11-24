import json

def save_expenses(expenses):
    with open("expenses.json","w") as file:
        json.dump(expenses,file)
def load_expenses():
    try:
        with open("expenses.json","r") as file:
            expenses=json.load(file)
            return expenses
    except FileNotFoundError:
            return []    
    except json.JSONDecodeError:
        return []
        
def add(expenses): 
    category=input("Category:").strip()
    if not category or category.isdigit():
        print("Enter a valid category!\n")
        return

    try:
        amount=int(input("Amount:"))
        
    except ValueError:
        print("Enter a valid number\n")
        return
    if amount<=0:
        print("Enter a valid number\n")
        return
    
    
    description=input("Description:").strip()
    if not description:
        print("Enter a description\n")
        return
    expense={}
    expense["category"]=category
    expense["amount"]=amount
    expense["description"]=description
    expenses.append(expense)
    print()
    save_expenses(expenses)
def view(expenses):
    if not expenses:
            print("no expenses\n")
            return
    print("YOUR EXPENSES")
    print()

    for exp in expenses:
        print(f"Category:{exp['category']}")
        print(f"Amount:{exp['amount']}")
        print(f"Description:{exp['description']}")
        print()

def calculate_total(expenses):
    total=0
    for exp in expenses:
        total+=exp["amount"]
    return total
    

def category_summary(expenses):
    print("Category Summary")
    print()
    result={}
    if not expenses:
        print("no expenses")
        return
    for exp in expenses:
        category=exp["category"]
        amount=exp["amount"]
        if category not in result:
            result[category]=amount
        else:
            result[category]+=amount
    for category,amount in result.items():
        print(f"{category}:{amount}")
    print()
def main():
    expenses=load_expenses() 

    while True:
        print("EXPENSE TRACKER")
        print("1.Add Expense\n2.View Expense\n3.Calculate Total\n4.Category Summary\n5.Exit")
        print()
        try:
            choice=int(input("Enter your choice:"))
            print()
            if choice==5:
                print("Thank you for using Expense Tracker!")
                break
            elif choice==1:
                add(expenses)
            elif choice==2:
                view(expenses)
            elif choice==3:
                total=calculate_total(expenses)
                print(f"Total expense is {total}")
                print()
            elif choice==4:
                category_summary(expenses)
            else:
                print("invalid choice\n")
        except ValueError:
            print("Please enter a valid choice")
            print()

if __name__ == "__main__":
    main()


