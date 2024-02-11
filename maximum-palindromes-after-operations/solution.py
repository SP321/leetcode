class Solution:
    def maxPalindromesAfterOperations(self, words):
        total_counts = Counter()
        for word in words:
            total_counts += Counter(word)

        total_p, total_o = 0, 0
        for ch in ascii_lowercase:
            total_p += total_counts[ch] // 2
            total_o += total_counts[ch] % 2

        sizes = [len(word) for word in words]
        ans=0
        for sz in sorted(sizes):
            odd_needed=sz%2
            pairs_needed=sz//2
            if total_p>=pairs_needed and total_o>=odd_needed:
                total_p-=pairs_needed
                total_o-=odd_needed
                ans+=1
            elif total_p>=pairs_needed+1 and odd_needed==1:
                total_p-=pairs_needed+1
                total_o+=1
                ans+=1
        return ans