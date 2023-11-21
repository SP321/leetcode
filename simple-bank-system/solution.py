class Bank:

    def __init__(self, balance: List[int]):
        self.x=balance
        print(len(self.x))

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1-1<len(self.x) and  account2-1<len(self.x) and self.x[account1-1]>=money:
            self.x[account2-1]+=money
            self.x[account1-1]-=money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account-1<len(self.x):
            self.x[account-1]+=money
            return True
        return False
        

    def withdraw(self, account: int, money: int) -> bool:
        if account-1<len(self.x) and self.x[account-1]>=money:
            self.x[account-1]-=money
            return True
        return False

        

        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)