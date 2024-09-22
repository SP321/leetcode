class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        s=set(bannedWords)
        c=0
        for x in message:
            if x in s:
                c+=1
                if c==2:
                    return True
        return False