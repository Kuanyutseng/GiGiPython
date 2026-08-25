class Bankaccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance=balance
        
    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
            print(self.owner+ '存入'+ str(amount) + '元'+'目前餘額：'+ str(self.balance) + '元。')
        else:
            print('錯誤提示')
        
    def withdraw(self, amount):
        if amount>self.balance:
            print(self.owner + '提款失敗：餘額不足！當前餘額：'+ str(self.balance) + '元。')
            return False 
        elif amount>0 and self.balance>0:
            self.balance-=amount
            print(self.owner + '提款'+ str(amount) +'元'+'目前餘額'+ str(self.balance) +'元。')
            return True
        else:
            return False
    
def transfer(sender: Bankaccount, receiver: Bankaccount, amount): #為何不是先自定義名稱
    result = sender.withdraw(amount)
    if result is True :
        receiver.deposit(amount)
        print('轉帳成功！'+ sender.owner + '轉帳'+ str(amount) + '元給'+ receiver.owner + '。')
    else:
        print('轉帳失敗：'+ sender.owner + '餘額不足，無法轉帳給'+ receiver.owner + '。')
    
alice =  Bankaccount("alice", 40000)
bob =  Bankaccount("bob")

alice.deposit(500)

transfer(alice, bob, 4000)
print(alice.balance)
print(bob.balance)