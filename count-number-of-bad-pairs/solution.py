class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        """
            j-i!=nums[j]-nums[i]
            j-nums[j]!=i-nums[i]
        """
        n=len(nums)
        c=Counter()
        ans=n*(n-1)//2
        for i,x in enumerate(nums):
            diff=i-x
            ans-=c[diff]
            c[diff]+=1
        return ans        