class Solution {
public:
    bool isIsomorphic(string s, string t) {
        map<char, char> x;
        set<char> y;
        for (int i = 0; i < s.length(); ++i) {
            if (x.find(s[i]) == x.end()) {
                if (y.find(t[i]) == y.end())
                    y.insert(t[i]);
                else
                    return 0;
                x[s[i]] = t[i];
            }
            if (x[s[i]] != t[i])
                return 0;
        }
        return 1;
    }
};