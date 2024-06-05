class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        vector<int> c(26, INT_MAX);
        vector<string> ans;
        for (auto w : words) {
            vector<int> cur(26, 0);
            for (auto c : w) 
                ++cur[c - 'a'];
            for (auto i = 0; i < 26; ++i)
                c[i] = min(c[i], cur[i]);
        }
        for (auto i = 0; i < 26; ++i)
            for (auto j = 0; j < c[i]; ++j)
                ans.push_back(string(1, i + 'a'));
        return ans;
    }
};