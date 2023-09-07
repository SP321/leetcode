class Solution {
public:
    static const int memsize = 'z' - 'A' + 1;

    bool isValid(const vector<int>& counter1, const vector<int>& counter2) {
        for (int i = 0; i < 26; i++) {
            if (counter1[i] < counter2[i]) return false;
        }
        for (int i = memsize - 26; i < memsize; i++) {
            if (counter1[i] < counter2[i]) return false;
        }
        return true;
    }

    string minWindow(string s, string t) {
        vector<int> required(memsize, 0);
        for (char ch : t) {
            required[ch - 'A']++;
        }

        vector<int> current(memsize, 0);
        
        int left = 0, right = 0, n = s.size();
        int ansStart = 0, ansLength = n + 1;

        while (right < n) {
            current[s[right] - 'A']++;
            right++;

            while (isValid(current, required)) {
                if (right - left < ansLength) {
                    ansLength = right - left;
                    ansStart = left;
                }
                current[s[left] - 'A']--;
                left++;
            }
        }

        return ansLength != n + 1 ? s.substr(ansStart, ansLength) : "";
    }
};
