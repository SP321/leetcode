class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ans=0
        banned=set(banned)
        for x in range(1,n+1):
            if x>maxSum:
                break
            if x not in banned:
                maxSum-=x
                ans+=1
        return ans
