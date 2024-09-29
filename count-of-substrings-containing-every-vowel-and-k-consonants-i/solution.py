class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)

        def helper(k):
            ans = 0
            i = 0
            v=Counter()
            c=0
            for j in range(n):
                if word[j] in 'aeiou':
                    v[word[j]]+=1
                else:
                    c+=1
                while len(v)==5 and c>k:
                    if word[i] in 'aeiou':
                        v[word[i]]-=1
                        if v[word[i]]==0:
                            del v[word[i]]
                    else:
                        c-=1
                    i += 1
                ans += (j - i + 1)
            return ans

        return helper(k) - helper(k - 1)