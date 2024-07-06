class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n=len(colors)
        colors+=colors
        ans=0
        i=0
        for j in range(1,n+k-1):
            if colors[j]==colors[j-1]:
                i=j
            if j-i+1>=k:
                ans+=1
        return ans