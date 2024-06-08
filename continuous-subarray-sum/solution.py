class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        c={}
        c[0]=-1
        cur=0
        for i,x in enumerate(nums):
            cur+=x
            if cur%k in c:
                if c[cur%k]<i-1:
                    return True
            else:
                c[cur%k]=i
        return False

