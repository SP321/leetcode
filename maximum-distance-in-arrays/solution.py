class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mi = arrays[0][0]
        mx = arrays[0][-1]
        ans = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]
            a,b=arr[0],arr[-1]
            ans=max(ans,abs(a-mi),abs(a-mx))
            ans=max(ans,abs(b-mi),abs(b-mx))
            mi = min(mi, a)
            mx = max(mx, b)

        return ans