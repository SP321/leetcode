class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        a=[]
        for i,x in enumerate(word):
            a.append(x)
            if x==ch:
                return ''.join(a[::-1])+word[i+1:]
        return word