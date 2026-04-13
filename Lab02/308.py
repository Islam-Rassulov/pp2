class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
      
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        
        if amount > self.balance:
            return "Insufficient Funds"
        else:
            self.balance -= amount
            return self.balance


try:
   
    line = input().split()
    if len(line) == 2:
        initial_balance = int(line[0])
        withdrawal_amount = int(line[1])
       
        my_account = Account("User", initial_balance)
        
        
        result = my_account.withdraw(withdrawal_amount)
        print(result)
except EOFError:
    pass