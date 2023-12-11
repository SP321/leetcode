class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return sum([key for key,val in Counter(arr).items() if val>len(arr)/4])