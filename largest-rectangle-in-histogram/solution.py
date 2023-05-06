class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        x=[]
        ans=0;
        for i in range(len(heights)):
            start = i
            while  len(x)>0 and heights[x[-1]] > heights[i] :
                ans = max(ans, heights[x[-1]] *(i - x[-1]))
                start = x[-1]
                x.pop()
            heights[start]=heights[i]
            x.append(start)
        while len(x)>0:
            ans = max(ans,heights[x[-1]]*(len(heights)-x[-1]));
            x.pop()
        return ans