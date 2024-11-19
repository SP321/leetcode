class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans=[]
        n=max(len(num1),len(num2))
        num1=num1.zfill(n)
        num2=num2.zfill(n)
        carry=0
        for x,y in zip(num1[::-1],num2[::-1]):
            cur=int(x)+int(y)+carry
            carry=cur//10
            ans.append(str(cur%10))
        if carry!=0:
            ans.append(str(carry))
        return ''.join(ans[::-1])