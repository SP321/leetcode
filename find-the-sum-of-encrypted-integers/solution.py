class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans=0
        for x in nums:
            a=str(x)
            ans+=int(len(a)*max(a))
        return ans