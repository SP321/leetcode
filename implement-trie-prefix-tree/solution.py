class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def traverse(self,word,create=False):
        cur=self.root
        for c in word:
            i=ord(c)-ord("a")
            if not cur.children[i]:
                if not create:
                    return None
                cur.children[i] = TrieNode()
            cur=cur.children[i]
        return cur
        
    def insert(self, word: str) -> None:
        node = self.traverse(word,create=True)
        node.end=True


    def search(self, word: str) -> bool:
        node = self.traverse(word)
        return node and node.end

    def startsWith(self, prefix: str) -> bool:
        return self.traverse(prefix)



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)