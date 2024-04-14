class Solution:
    def findLatestTime(self, s: str) -> str:
        ans=""
        for h in range(12):
            for m in range(60):
                x=f"{str(h).zfill(2)}:{str(m).zfill(2)}"
                if all(b=='?' or a==b for a,b in zip(x,s)):
                    ans=x
        return ans