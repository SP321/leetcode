create_node=lambda:defaultdict(create_node)
class Trie:
    def __init__(self, words):
        self.root = create_node()
        for word in words:
            self.add(word)

    def add(self, word):
        cur_node = self.root
        for letter in word:
            cur_node = cur_node[letter]

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        tr=Trie(words)
        n=len(target)
        @cache
        def dp(i):
            if i==n:
                return 0
            cur_node=tr.root
            ans=inf
            for j in range(i,n):
                if target[j] not in cur_node:
                    break
                ans=min(ans,dp(j+1)+1)
                cur_node = cur_node[target[j]]
            return ans
        ans=dp(0)
        return ans if ans!=inf else -1