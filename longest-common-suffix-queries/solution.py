create_node=lambda:defaultdict(create_node,{"_data":(inf,inf)})
class Trie:
    def __init__(self, words):
        self.root = create_node()
        for i,word in enumerate(words):
            self.add(word,i)

    def add(self, word,ix):
        self.root["_data"]=min(self.root["_data"],(len(word),ix))
        cur_node = self.root
        for letter in word[::-1]:
            cur_node = cur_node[letter]
            cur_node["_data"]=min(cur_node["_data"],(len(word),ix))

    def __getitem__(self, word):
        cur_node = self.root
        for letter in word[::-1]:
            if letter not in cur_node:
                break 
            cur_node = cur_node[letter]
        return cur_node["_data"][1]

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        tr=Trie(wordsContainer)
        return [tr[x] for x in wordsQuery]