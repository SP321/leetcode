class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s==goal[i:]+goal[:i]:
                return True
        return False
    
        