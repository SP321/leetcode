class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.append([0,0])
        items.sort()
        n=len(items)
        for i in range(1,n):
            items[i][1]=max(items[i][1],items[i-1][1])
        ans=[]
        for x in queries:
            pos=bisect_right(items,[x,inf])-1
            ans.append(items[pos][1])
        return ans