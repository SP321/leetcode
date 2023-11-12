class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        a,b=nums1[-1],nums2[-1]
        ans=0
        for i in range(n-1):
            a,b=nums1[i],nums2[i]
            if a>nums1[-1] or b>nums2[-1]:
                a,b=b,a
                ans+=1
            if a>nums1[-1] or b>nums2[-1]:
                return -1
        ans2=1
        for i in range(n-1):
            a,b=nums1[i],nums2[i]
            if a>nums2[-1] or b>nums1[-1]:
                ans2+=1
        return min(ans2,ans)