class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c=Counter(nums1)
        c2=Counter(nums2)
        ans=[]
        for x,y in c.items():
            ans.extend([x]*min(y,c2[x]))
        return ans
        