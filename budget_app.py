def truncate(number):
    multiplier = 10
    return int(number * multiplier) / multiplier

def get_total(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.total_withdraw()
        breakdown.append(category.total_withdraw())
    rounded = list(map(lambda x: truncate(x/total), breakdown))
    return rounded

def create_spend_chart(categories):
    res = "Percentage spent by category\n"
    i = 100
    totals = get_total(categories)
    while i >= 0:
        cat_spaces = " "
        for total in totals:
            if total * 100 >= i:
                cat_spaces += "o  "
            else:
                cat_spaces += "   "
        res+= str(i).rjust(3) + "|" + cat_spaces + ("\n")
        i -= 10
        
    dashes = "-" + "---" * len(categories)
    names = []
    x_axis = ""
    for category in categories:
        names.append(category.name)
        
    maxi = max(names, key = len)
    
    for x in range(len(maxi)):
        name_str = '     '
        for name in names:
            if x >= len(name):
                name_str += "   "
            else:
                name_str += name[x] + "  "
                
        if(x != len(maxi) - 1):
            name_str += '\n'
            
        x_axis += name_str
    res += dashes.rjust(len(dashes)+4) + "\n" + x_axis
    return res

class Category:


    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        total = 0
        elements = ""
        category_name = f"{self.name:*^30}"
        for i in self.ledger:
            elements += f"{i['description'][0:23]:23}" + f"{i['amount']:>7.2f}" + '\n'
            total += i['amount']

        result = f"{category_name}" + "\n" + f"{elements}" + "Total: " + str(total)
        return result  

    def deposit(self, amount, description=""):
        deposit_dict = {"amount": amount, "description": description}
        self.ledger.append(deposit_dict)
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True


    def withdraw(self, amount, description=""):
        withdraw_amount = -amount
        withdraw_dict = {
        "amount": withdraw_amount,
        "description":description
        }
        if self.check_funds(amount):
            self.ledger.append(withdraw_dict)
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False
    
    def total_withdraw(self):
        total = 0 
        for i in self.ledger:
            if i['amount']< 0:
                total += i['amount']
                
        return total
