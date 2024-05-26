class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans=0
        n=len(nums1)
        m=len(nums2)
        for i in range(n):
            for j in range(m):
                if nums2[j]*k<=nums1[i] and nums1[i]%(nums2[j]*k)==0:
                    ans+=1
        return ans