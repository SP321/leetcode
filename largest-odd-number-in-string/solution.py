class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in list(num[::-1]):
          if int(i)&1:
            break
          num=num[:-1]
        return num