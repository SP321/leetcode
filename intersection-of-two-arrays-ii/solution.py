class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        c1=Counter(nums1)
        c2=Counter(nums2)
        for x in c1:
            if x in c2:
                ans.extend([x]*min(c1[x],c2[x]))
        return ans