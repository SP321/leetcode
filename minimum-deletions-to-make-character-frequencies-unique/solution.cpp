class Solution {
public:
    int minDeletions(string s) {
        vector<int> freq(26, 0);
        int ans = 0;

        for (char c : s) {
            freq[c - 'a']++;
        }

        unordered_map<int,bool> seen;

        for (int f : freq) {
            while (f > 0 && seen[f]) {
                f--;
                ans++;
            }
            seen[f] = true;
        }

        return ans;
    }
};