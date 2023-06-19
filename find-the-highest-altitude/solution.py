class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        x=ans=0
        for i in gain:
            x+=i
            ans=max(ans,x)
        return ans