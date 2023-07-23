class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans=[]
        for i in words:
            z=i.split(separator)
            ans.extend([j for j in z if len(j)>0])
        return ans
        