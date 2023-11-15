class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        for c in s:
            if c == '(':
                leftMin += 1
                leftMax += 1
            if c == ')':
                leftMin -= 1
                leftMax -= 1
            if c == '*':
                leftMin -= 1
                leftMax += 1
            
            leftMin=max(0,leftMin)
            if leftMax < 0:
                return False
        
        return leftMin == 0