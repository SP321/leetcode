class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends=set(deadends)
        if "0000" in deadends:
            return -1
        def get_nei(x):
            ans=[]
            for i in range(4):
                cur=str((int(x[i])+1)%10)
                a=x[:i]+cur+x[i+1:]
                if a not in deadends:
                    ans.append(a)
            for i in range(4):
                cur=str((int(x[i])+9)%10)
                a=x[:i]+cur+x[i+1:]
                if a not in deadends:
                    ans.append(a)
            return ans
        deadends.add("0000")
        q=["0000"]
        ans=0
        while q:
            q2=[]
            for x in q:
                if x==target:
                    return ans
                for nei in get_nei(x):
                    deadends.add(nei)
                    q2.append(nei)
            q=q2
            ans+=1
        return -1