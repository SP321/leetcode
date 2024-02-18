class Trie:

    def __init__(self):
        self.root={}

    def insert(self, word: str) -> None:
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, dict())
        current_dict['_end_'] = 1

    def search(self, word: str) -> bool:
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return '_end_' in current_dict

    def startsWith(self, prefix: str) -> bool:
        current_dict = self.root
        for letter in prefix:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)