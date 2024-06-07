create_node=lambda:defaultdict(create_node,{"_":None})
class Trie:
    def __init__(self, words):
        self.root = create_node()
        for i,word in enumerate(words):
            self.add(word,i)

    def add(self, word,ix):
        cur_node = self.root
        for letter in word:
            cur_node = cur_node[letter]
        cur_node["_"]=word

    def __getitem__(self, word):
        cur_node = self.root
        for letter in word:
            if letter not in cur_node:
                break 
            cur_node = cur_node[letter]
            if cur_node["_"]:
                return cur_node["_"]
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tr=Trie(dictionary)
        return ' '.join(tr[x] for x in sentence.split())
