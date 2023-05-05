class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        c=0
        i=0
        j=0
        ans=0
        n=len(s)
        while j<k:
            if s[j] in "aeiou":
                c+=1
            ans=c
            j+=1
        while j<n:
            if s[j] in "aeiou":
                c+=1
            j+=1
            if s[i] in "aeiou":
                 c-=1
            i+=1
            ans=max(ans,c)
        return ans
            