class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        a=[]
        b=[]
        c=defaultdict(int)
        ma=0
        for i,j in zip(s,goal):
            if i!=j:
                a.append(i)
                b.append(j)
            c[i]+=1
            ma=max(ma,c[i])
        if len(a)==2 and a==b[::-1]:
            return True
        if s==goal and ma>1:
            return True
        return False
