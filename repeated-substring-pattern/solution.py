class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n=len(s)
        for i in range(n//2,0,-1):
            if n%i==0: 
                if s[:i]*(n//i)==s:
                    return True
        return False
        