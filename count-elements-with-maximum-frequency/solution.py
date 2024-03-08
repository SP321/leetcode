class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c=Counter(nums)
        cur=-1
        ans=0
        for val,x in c.most_common():
            if x<cur:
                break
            ans+=x
            cur=x
        return ans