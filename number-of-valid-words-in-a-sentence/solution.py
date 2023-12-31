class Solution:
    def countValidWords(self, sentence: str) -> int:
        ans = 0
        for word in sentence.split():
            if word[0] == "-" or word[0] in "!.," and len(word) > 1:
                continue
            hyphens = 0
            for i, x in enumerate(word):
                if x in "0123456789":
                    break
                if x == "-":
                    if hyphens == 0 and 0 < i < len(word) - 1 and word[i + 1].isalpha():
                        hyphens += 1
                    else:
                        break
                if x in "!.," and i != len(word) - 1:
                    break
            else:
                ans += 1
        return ans