class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d=defaultdict(list)
        en=False
        for word in wordList:
            for i in range(len(word)):
                d[word[:i]+"."+word[i+1:]].append(word)
            if word==endWord:
                en=True
        enqueued=set()
        q=[beginWord]
        enqueued.add(beginWord)
        ans=1
        while q:
            ans+=1
            q2=[]
            for word in q:
                for i in range(len(word)):
                    for j in d[word[:i]+"."+word[i+1:]]:
                        if j==endWord:
                            return ans
                        if j not in enqueued:
                            q2.append(j)
                            enqueued.add(j)
            q=q2
        return 0
