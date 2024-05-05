class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def key_func(k):
            i=0
            ans=0
            for j in range(len(nums)):
                while i<j and nums[j]-nums[i]>k:
                    i+=1
                ans+=j-i
            return ans
        return bisect_left(range(10**6+1),k,key=key_func)