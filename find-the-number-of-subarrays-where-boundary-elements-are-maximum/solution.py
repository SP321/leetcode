
class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        d=defaultdict(list)
        for i,x in enumerate(nums):
            d[x].append(i)

        ng = [n] * n
        st = []
        for i in range(n):
            while st and nums[i] > nums[st[-1]]:
                ng[st.pop()] = i
            st.append(i)

        ans=0
        for pos_list in d.values():
            i = 0
            for j in range(len(pos_list)):
                while i<j and ng[pos_list[i]]<=pos_list[j]:
                    i += 1
                ans += j-i+1
        return ans