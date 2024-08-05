class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c=Counter(arr)
        for x in arr:
            if c[x]==1:
                k-=1
            if k==0:
                return x
        return ""