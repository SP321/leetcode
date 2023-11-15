class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ans=1
        for i in arr[1:]:
            ans=min(ans+1,i)
        return ans        