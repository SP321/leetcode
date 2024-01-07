class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n,sa,sb=len(nums1),set(nums1),set(nums2)
        return min(n,min(len(sa-sb),n//2)+min(len(sb-sa),n//2)+len(sa&sb))
            