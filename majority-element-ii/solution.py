class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        return [i for i in c if c[i]>len(nums)//3]