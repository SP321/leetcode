class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a,b=0,0
        c=Counter()
        arr=[]
        for x,y in zip(secret,guess):
            if x==y:
                a+=1
            else:
                c[x]+=1
                arr.append(y)
        for x in arr:
            if c[x]:
                b+=1
                c[x]-=1

        return f"{a}A{b}B"