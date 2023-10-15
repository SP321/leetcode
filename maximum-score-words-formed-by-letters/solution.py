class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        ans = 0
        def backtrack(index, letter_count, curr_sum):
            nonlocal ans
            if index == len(words):
                ans = max(ans, curr_sum)
                return
            
            word = words[index]

            temp = letter_count[:]

            curr_word_sum = 0
            valid = True
            for c in word:
                if letter_count[ord(c)-97] == 0:
                    valid = False
                    break
                curr_word_sum += score[ord(c)-97]
                letter_count[ord(c)-97] -= 1

            if valid:
                backtrack(index+1, letter_count, curr_sum+curr_word_sum)
            
            letter_count = temp[:]
            
            backtrack(index+1, letter_count, curr_sum)

        letter_count = [0]*26
        for c in letters:
            letter_count[ord(c)-97] += 1
        
        backtrack(0, letter_count, 0)
        return ans