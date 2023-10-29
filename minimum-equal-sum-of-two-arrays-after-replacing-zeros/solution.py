class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        c1=0
        z1=0
        z2=0
        c2=0
        for i in nums1:
            if i==0:
                z1+=1
                c1+=1
            c1+=i
        for i in nums2:
            if i==0:
                z2+=1
                c2+=1
            c2+=i
        if c1<c2:
            z=z1
        elif c2<c1:
            z=z2
        else:
            return c1
        if z==0:
            return -1
        return max(c1,c2)