class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        used = set()
        for i in range(len(words)):
            if words[i] not in used:
                for j in range(i+1, len(words)):
                    if words[i] == words[j][::-1] and words[j] not in used:
                        ans += 1
                        used.add(words[i])
                        used.add(words[j])
                        break
        return ans