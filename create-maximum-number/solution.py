class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def k_largest_sequence(nums, k):
            drop = len(nums) - k
            ans = []
            for num in nums:
                while drop and ans and ans[-1] < num:
                    ans.pop()
                    drop -= 1
                ans.append(num)
            return ans[:k]

        def merge(a, b):
            return [max(a, b).pop(0) for _ in a+b]

        ans=[]
        for i in range(max(0, k-len(nums2)),min(len(nums1),k)+1):
            j=k-i
            x=merge(k_largest_sequence(nums1, i), k_largest_sequence(nums2, j))
            ans=max(ans,x)
        return ans
      