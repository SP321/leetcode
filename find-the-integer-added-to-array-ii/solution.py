class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        diffs=[nums2[0]-x for x in nums1[:3]]

        for diff in sorted(diffs):
            i=0
            j=0
            while i<len(nums1) and j<len(nums2):
                if nums2[j]-nums1[i]==diff:
                    i+=1
                    j+=1
                else:
                    i+=1
            if j==len(nums2):
                return diff