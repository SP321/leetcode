class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        a=sentence.split()
        a.append(a[0])
        for x,y in pairwise(a):
            if x[-1]!=y[0]:
                return False
        return True