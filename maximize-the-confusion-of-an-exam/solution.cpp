class Solution {
public:
    int maxConsecutiveAnswers(string answerKey, int k) {
        map<char, int> count;
        int max_freq = 0, max_count = 0, left = 0;

        for (int right = 0; right < answerKey.size(); right++) {
            count[answerKey[right]]++;
            max_freq = max(max_freq, count[answerKey[right]]);
            
            if ((right - left + 1) - max_freq > k) {
                count[answerKey[left]]--;
                left++;
            }
            
            max_count = max(max_count, right - left + 1);
        }

        return max_count;
    }
};