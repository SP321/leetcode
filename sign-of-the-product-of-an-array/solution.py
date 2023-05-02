class Solution:
    def arraySign(self, nums: List[int]) -> int:
        odc=0
        for i in nums:
            if i==0:
                return 0
            if i<0:
                odc+=1
        if odc%2==0:
            return 1
        return -1