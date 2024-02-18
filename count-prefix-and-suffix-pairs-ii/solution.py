create_node=lambda:defaultdict(create_node,{"end_count":0})
class Trie:
    def __init__(self):
        self.root = create_node()

    def count_add(self, word):
        cur = self.root
        ans=0
        for key in zip(word,word[::-1]):
            cur=cur[key]
            ans+=cur['end_count']
        cur['end_count'] += 1
        return ans

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        tr = Trie()
        return sum(tr.count_add(word) for word in words)