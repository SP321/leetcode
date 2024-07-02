class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        c=0            
        for x in arr:
            if x&1:
                c+=1
            else:
                c=0
            if c>2:
                return True
        return False