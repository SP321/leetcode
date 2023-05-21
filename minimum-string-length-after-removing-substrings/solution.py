class Solution:
    def minLength(self, s: str) -> int:
        def rem(s):
            s=s.replace('AB','')
            s=s.replace('CD','')
            print(s)
            return s
        while('AB' in s or 'CD' in s):
            s=rem(s)
        return len(s)