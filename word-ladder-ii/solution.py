class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        wordList = set(wordList)
        wordList.add(beginWord)
        g = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList and next_word != word:
                        g[word].append(next_word)

        q = deque([beginWord])
        parents = defaultdict(list)
        visited = set()
        found = False
        level = {beginWord: 0}
        
        while q and not found:
            for _ in range(len(q)):
                word = q.popleft()
                for neighbor in g[word]:
                    if neighbor not in level:
                        level[neighbor] = level[word] + 1
                        q.append(neighbor)
                    if level[neighbor] == level[word] + 1:
                        parents[neighbor].append(word)
                    if neighbor == endWord:
                        found = True

        def build_paths(word):
            if word == beginWord:
                return [[beginWord]]
            paths = []
            for parent in parents[word]:
                for path in build_paths(parent):
                    paths.append(path + [word])
            return paths

        return build_paths(endWord) if found else []

