class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        ans = {}
        for num in nums2:
            while st and st[-1] < num:
                ans[st.pop()] = num
            st.append(num)
        del st
        return [ans[num] if num in ans else -1 for num in nums1]