create_node=lambda:defaultdict(create_node,{"_":(inf,inf)})
class Trie:
    def __init__(self, words):
        self.root = create_node()
        for i,word in enumerate(words):
            self.add(word,i)

    def add(self, word,ix):
        self.root["_"]=min(self.root["_"],(len(word),ix))
        cur_node = self.root
        for letter in word[::-1]:
            cur_node = cur_node[letter]
            cur_node["_"]=min(cur_node["_"],(len(word),ix))

    def __getitem__(self, word):
        cur_node = self.root
        for letter in word[::-1]:
            if letter not in cur_node:
                break 
            cur_node = cur_node[letter]
        return cur_node["_"][1]

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        tr=Trie(wordsContainer)
        return [tr[x] for x in wordsQuery]