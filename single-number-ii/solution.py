class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        for i in nums:
            if d[i]==1:
                return i
        