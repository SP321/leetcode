class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        s=set(int(i,2) for i in nums)
        for i in range(n+1):
            if i not in s:
                return bin(i)[2:].zfill(n)