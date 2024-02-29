class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        class customStr(str):
            def __lt__(x,y):
                return x+y > y+x
        ans=''.join(sorted([customStr(x) for x in nums]))
        return ans if ans[0]!='0' else '0'