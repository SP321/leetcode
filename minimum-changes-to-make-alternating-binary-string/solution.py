class Solution:
    def minOperations(self, s: str) -> int:
        ans1=0
        ans2=0
        for i,x in enumerate(s):
            if int(s[i])!=i%2:
                ans2+=1
            if int(s[i])==i%2:
                ans1+=1
        assert(ans1==len(s)-ans2)
        return min(ans1,ans2)
