class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        pairs=list(zip(plantTime,growTime))
        mx,days=0,0
        pairs.sort(key=lambda x:(-x[1],x[0]))
        for i in range(len(plantTime)):
            mx=max(mx,(days+pairs[i][0]+pairs[i][1]))
            days+=pairs[i][0]
        return mx