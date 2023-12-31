class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        unordered_map<char, int> f;
        int ans = -1;
        for (int i = 0; i < s.size(); i++) {
            if (f.find(s[i]) == f.end())
                f[s[i]] = i+1;
            else
                ans = max(ans, i - f[s[i]]);
        }
        return ans;
    }
};