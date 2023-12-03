class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        prefix_counts = defaultdict(lambda:Counter())
        c=Counter()
        ans = 0

        def check_counts(left_c,cur_c):
            c=cur_c-left_c
            for count in c.values():
                if count==0:
                    continue
                if count==k:
                    continue
                return 0
            return 1

        i=0
        for j, char in enumerate(word):
            if abs(ord(char) - ord(word[j - 1])) > 2:
                c=Counter()
                prefix_counts = defaultdict(lambda:Counter())
                i=j
            c[char]+=1
            if c[char]>=k:
                for back in range(j-k,max(i,j-26*k)-2,-k):
                    ans+= check_counts(prefix_counts[back],c)
            prefix_counts[j] = c.copy()
        return ans