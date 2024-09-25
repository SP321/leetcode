from collections import defaultdict
create_node=lambda:defaultdict(create_node,{"ec":0}) #ec is count of words end at node.

class Trie:
    def __init__(self, words):
        self.root = create_node()
        for word in words:
            self.add(word)

    def add(self, word):
        cur_node = self.root
        for letter in word:
            cur_node = cur_node[letter]
            cur_node["ec"] +=1

    def __getitem__(self, word):
        cur_node = self.root
        ans=0
        for letter in word:
            if letter not in cur_node:
                break
            cur_node = cur_node[letter]
            ans+=cur_node['ec']
        return ans

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        tr=Trie(words)
        return [tr[x] for x in words]
        