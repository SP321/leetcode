class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time%=(n-1)*2
        if time<n:
            return time+1
        time-=n-1
        return n-time