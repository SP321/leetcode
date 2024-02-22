class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        create_node=lambda:defaultdict(create_node,{"_e":0})
        root = create_node()
        def count_add(word):
            cur = root
            ans=0
            for key in zip(word,word[::-1]):
                cur=cur[key]
                ans+=cur['_e']
            cur['_e'] += 1
            return ans
        return sum(map(count_add,words))