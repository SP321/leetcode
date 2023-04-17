class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        y=x
        while x>0:
            rev=rev*10+x%10
            x//=10
        return y==rev