class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        a=[1 if x else -1 for x in possible]
        s=sum(a)
        cur=0
        for i,x in enumerate(a[:-1]):
            cur+=x
            if cur>s-cur:
                return i+1
        return -1