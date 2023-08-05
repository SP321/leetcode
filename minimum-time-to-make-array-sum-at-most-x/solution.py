class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n=len(nums1)
        arr = sorted([(nums1[i], nums2[i]) for i in range(n)],key=lambda x:[-x[1],x[0]])
        @lru_cache(4900)
        def dp(i,to_pick):
            if i==n or to_pick==0:
                return 0
            leave=dp(i+1,to_pick)
            take=arr[i][0]+(to_pick)*arr[i][1] + dp(i+1,to_pick-1)
            return max(take,leave)
        s1=sum(nums1)
        s2=sum(nums2)
        for i in range(n+1):
            total = s1+i*s2
            if total-dp(0,i)<=x:
                return i
        return -1