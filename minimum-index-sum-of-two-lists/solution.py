class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans=[]
        d={}
        for i,a in enumerate(list1):
            d[a]=i
        mi=inf
        for i,a in enumerate(list2):
            if a in d:
                mi=min(mi,d[a]+i)
                ans.append((d[a]+i,a))
        return [x for i,x in ans if i==mi]