class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        x=[a%2==b%2 for a,b in pairwise(nums)]
        pref=list(accumulate(x,initial=0))
        ans=[]
        for i,j in queries:
            ans.append(pref[j]-pref[i]==0)
        return ans