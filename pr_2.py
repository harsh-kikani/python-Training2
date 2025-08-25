'''class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
        
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance =", self.get_balance())
        
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.get_balance())
        
    def get_balance(self):
        return self.balance
    
acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)'''

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print("Factorial is:", fact)

n = int(input("Enter a number: ")) 
cal_fact(n)
    
