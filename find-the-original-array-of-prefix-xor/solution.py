class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        prev=0
        ans=[]
        for i in pref:
            ans.append(prev^i)
            prev=i
        return ans