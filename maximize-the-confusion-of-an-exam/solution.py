class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_freq = max_count = left = 0
        count = {'T': 0, 'F': 0}
        
        for right in range(len(answerKey)):
            count[answerKey[right]] += 1
            max_freq = max(max_freq, count[answerKey[right]])
            
            if (right - left + 1) - max_freq > k:
                count[answerKey[left]] -= 1
                left += 1
            
            max_count = max(max_count, right - left + 1)
        
        return max_count