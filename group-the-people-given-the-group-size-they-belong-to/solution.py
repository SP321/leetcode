class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d=defaultdict(list)
        n=len(groupSizes)
        for i in range(n):
            d[groupSizes[i]].append(i)
        ans=[]
        for i in d:
            x=d[i]
            for j in range(0,len(x),i):
                ans.append(x[j:j+i])
        return ans