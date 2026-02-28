class account:
    def __init__(self,acc_no,balance):
        self.acc_no=acc_no
        self.balance=balance
    def credit(self,amt):
        self.balance+=amt
        print(amt,"credited")

    def debit(self,amt):
        self.balance-=amt
        print(amt,"debited")

    def print_balance(self):
        print("your current balance is:",self.balance)


acc_num=int(input("enter your account number"))
bal=int(input("eneter your bank balance"))
ac1=account(acc_num,bal)
ac1.credit(200)
ac1.print_balance()
ac1.debit(850)
ac1.print_balance()    