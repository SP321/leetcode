class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums=nums[::-1]
        s=list(range(1,k+1))
        for i in range(len(nums)):
            if sorted(set(nums[:i+1]))[:k]==s:
                return i+1
        return -1
            
        