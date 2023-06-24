class Solution {
public:
    int characterReplacement(string s, int k) {
         if(s.length() == 0 || s.length() == 1)
            return s.length();
        int kk = k;
        int i = 0;
        int max_count = 0;
        map<char, int> counts;
        for(int j = 0; j < s.length(); j++) {
            char c = s[j];
            counts[c]++;
            if(counts[c] > max_count) {
                max_count = counts[c];
            } else {
                kk--;
            }
            if(kk < 0) {
                counts[s[i]]--;
                i++;
                kk++;
            }
        }
        return max_count + k - kk;
    }
};