class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        c=Counter(''.join(words))
        for i in c.values():
            if i%len(words)!=0:
                return False
        return True