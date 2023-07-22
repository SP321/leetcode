class Solution:
    def sortVowels(self, s: str) -> str:
        x=[i for i in s]
        m=[i for i in range(len(x)) if x[i] in "aeiouAEIOU"]
        for i,j in zip(m,sorted(m,key=lambda a:s[a])):
            x[i]=s[j]
        return ''.join(x)