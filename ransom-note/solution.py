class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a=Counter(ransomNote)
        b=Counter(magazine)
        for i in a.keys():
            if b[i]<a[i]:
                return False
        return True