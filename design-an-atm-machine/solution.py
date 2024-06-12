class ATM:
    def __init__(self):
        self.c=[0]*5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.c[i]+=banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        cur=[0]*5
        for i,x in enumerate([500,200,100,50,20]):
            a=min(self.c[4-i],amount//x)
            cur[4-i]+=a
            amount-=x*a
        if amount!=0:
            return [-1]
        for i in range(5):
            self.c[i]-=cur[i]
        return cur


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)