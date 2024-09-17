class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [key for key,cnt in Counter(s1.split()+s2.split()).items() if cnt==1]