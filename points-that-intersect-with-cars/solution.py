class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        x=[False for i in range(101)]
        for start,end in nums:
            for i in range(start,end+1):
                x[i]=True
        return sum(x)
    