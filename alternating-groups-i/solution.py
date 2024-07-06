class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        ans=0
        for i in range(len(colors)):
            if colors[i]!=colors[i-1] and colors[i]!=colors[(i+1)%len(colors)]:
                ans+=1
        return ans