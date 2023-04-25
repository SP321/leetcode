class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        x=sorted(arr)
        d=x[1]-x[0];
        for i in range(1,len(x)):
            if d!=x[i]-x[i-1]:
                return False
        return True