class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        @cache
        def backtrack(s: str) -> tuple[bool, list[str]]:
            if not s:
                return [""]
            sentences = []
            for i in range(1, len(s) + 1):
                word = s[:i]
                if word in word_set:
                    next_sentences = backtrack(s[i:])
                    if len(next_sentences)>0:
                        for sentence in next_sentences:
                            if len(sentence)>0:
                                sentences.append(word + " " + sentence)
                            else:
                                sentences.append(word)
            return sentences

        ans = backtrack(s)
        return ans