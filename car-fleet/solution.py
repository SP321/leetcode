class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)
        maxt=0
        ans=0
        for pos,sped in sorted(zip(position, speed))[::-1]:
            t=(target-pos)/sped
            if t>maxt :
                maxt=t
                ans+=1
        return ans