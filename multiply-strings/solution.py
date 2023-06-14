class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        ans=[]
        startpos=0
        def add(pos,y):
            while len(ans)<=pos:
                ans.append(0)
            y+=ans[pos]
            ans[pos]=(y)%10
            if y>=10:
                add(pos+1,(y)//10)
        for i in num2[::-1]:
            pos=startpos
            for j in num1[::-1]:
                x,y=ord(i)-ord('0'),ord(j)-ord('0')
                t=x*y
                add(pos,t)
                pos+=1
            startpos+=1
        return ''.join(str(i) for i in ans[::-1])