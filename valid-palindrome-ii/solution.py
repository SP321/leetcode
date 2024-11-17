class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(s):
            s=deque(s)
            while s and s[0]==s[-1]:
                s.popleft()
                if s:
                    s.pop()
            return ''.join(s)
        if len(helper(s[1:]))==0 or len(helper(s[:-1]))==0:
            return True
        s=helper(s)
        if len(s)==0 or len(helper(s[1:]))==0 or len(helper(s[:-1]))==0:
            return True
        return False